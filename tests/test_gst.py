import json
from pathlib import Path
import pytest
from src.agent import make_graph
DATA=json.loads(Path('fixtures/gst_cases_v1.json').read_text())['cases']
@pytest.mark.parametrize('case',DATA,ids=[x['id'] for x in DATA])
def test_clean_candidate(case):
    result=make_graph().invoke({'case':case,'defect':'none'})
    assert result['tax_paise']==case['expected_tax_paise']
    assert result['tax_type']==case['expected_type']
    assert result['rule_id']==case['tax_code']

def test_same_amount_wrong_rule_detectable_by_trace():
    c=next(x for x in DATA if x['id']=='INV009')
    s=make_graph().invoke({'case':c,'defect':'wrong_rule_same_amount'})
    assert s['tax_paise']==c['expected_tax_paise']
    assert s['rule_id']!=c['tax_code']
