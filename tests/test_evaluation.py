
from scripts.evaluate import build_agent, evaluate, summarize


def test_baseline_accuracy():
    """Verify the baseline agent achieves 100% accuracy."""
    results = evaluate(build_agent())
    metrics = summarize(results)

    assert metrics["accuracy"] == 1.0


def test_introduced_regression_is_detectable():
    """Verify the faulty agent drops to 70% accuracy."""
    results = evaluate(build_agent(regressed=True))
    metrics = summarize(results)

    assert metrics["accuracy"] == 0.7
