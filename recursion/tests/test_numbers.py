import json
import pytest
from recursion.numbers import sum_up_to, sum_even, sum_between

with open("recursion/tests/test_numbers_cases.json") as f:
    cases = json.load(f)

@pytest.mark.parametrize("inp,expected", cases["sum_up_to"])
def test_sum_up_to(inp, expected):
    if 'sum_up_to' not in globals():
        pytest.skip("sum_up_to() not implemented yet")
    assert sum_up_to(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["sum_even"])
def test_sum_even(inp, expected):
    if 'sum_even' not in globals():
        pytest.skip("sum_even() not implemented yet")
    assert sum_even(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["sum_between"])
def test_sum_between(inp, expected):
    if 'sum_between' not in globals():
        pytest.skip("sum_between() not implemented yet")
    # If inp is a list of arguments, unpack with *
    assert sum_between(*inp) == expected
