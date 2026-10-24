"""Deterministic continuous regression evaluation proof of concept."""
import argparse
import csv
import json
from pathlib import Path
from time import perf_counter

from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict

class State(TypedDict):
    task: str
    category: str
    response: str


def build_agent(regressed=False):
    def classify(state: State):
        task = state['task'].lower()
        if 'refund' in task:
            category = 'general' if regressed else 'refund'
        elif 'invoice' in task:
            category = 'invoice'
        else:
            category = 'general'
        return {'category': category}

    def respond(state: State):
        return {'response': f"Route to {state['category']} support."}

    graph = StateGraph(State)
    graph.add_node('classify_task', classify)
    graph.add_node('generate_response', respond)
    graph.add_edge(START, 'classify_task')
    graph.add_edge('classify_task', 'generate_response')
    graph.add_edge('generate_response', END)
    return graph.compile()

CASES = [
    ('I need a refund', 'refund'),
    ('Where is my refund?', 'refund'),
    ('Please process a refund', 'refund'),
    ('I need help with my invoice', 'invoice'),
    ('Where can I download my invoice?', 'invoice'),
    ('My invoice is incorrect', 'invoice'),
    ('Please explain this invoice', 'invoice'),
    ('Hello, I need support', 'general'),
    ('Can you help me?', 'general'),
    ('How do I contact support?', 'general'),
]


def evaluate(agent):
    rows = []
    for task, expected in CASES:
        start = perf_counter()
        result = agent.invoke({'task': task, 'category': '', 'response': ''})
        elapsed = (perf_counter() - start) * 1000
        rows.append({'task': task, 'expected': expected, 'actual': result['category'],
                     'correct': result['category'] == expected, 'latency_ms': round(elapsed, 3)})
    return rows


def summarize(rows):
    return {'cases': len(rows), 'accuracy': sum(r['correct'] for r in rows) / len(rows),
            'mean_latency_ms': round(sum(r['latency_ms'] for r in rows) / len(rows), 3)}


def run(regressed=False, output='artifacts', max_drop=0.0):
    baseline = evaluate(build_agent(False))
    candidate = evaluate(build_agent(regressed))
    base = summarize(baseline)
    cand = summarize(candidate)
    drop = base['accuracy'] - cand['accuracy']
    passed = drop <= max_drop and cand['accuracy'] >= 0.9
    out = Path(output)
    out.mkdir(parents=True, exist_ok=True)
    with (out / 'candidate_results.csv').open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=candidate[0].keys())
        writer.writeheader()
        writer.writerows(candidate)
    report = {'baseline': base, 'candidate': cand, 'accuracy_drop': round(drop, 4),
              'max_allowed_drop': max_drop, 'gate': 'PASS' if passed else 'BLOCK',
              'note': 'Illustrative fixed 10-case deterministic test suite; not production validation.'}
    (out / 'evaluation_report.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2))
    return passed


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--regressed', action='store_true', help='Inject known defect to validate gate')
    parser.add_argument('--output', default='artifacts')
    parser.add_argument('--max-drop', type=float, default=0.0)
    args = parser.parse_args()
    raise SystemExit(0 if run(args.regressed, args.output, args.max_drop) else 1)
