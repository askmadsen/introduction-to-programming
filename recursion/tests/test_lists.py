import json
import pytest
import recursion.lists as list

with open("recursion/tests/test_lists_cases.json") as f:
    cases = json.load(f)

@pytest.mark.parametrize("inp,expected", cases["length"])
def test_length(inp, expected):
    if not hasattr(list, "length"):
        pytest.skip("length() not implemented yet")
    assert list.length(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["count"])
def test_count(inp, expected):
    if not hasattr(list, "count"):
        pytest.skip("count() not implemented yet")
    assert list.count(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["member"])
def test_member(inp, expected):
    if not hasattr(list, "member"):
        pytest.skip("member() not implemented yet")
    assert list.member(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["subset"])
def test_subset(inp, expected):
    if not hasattr(list, "subset"):
        pytest.skip("subset() not implemented yet")
    assert list.subset(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["set_equals"])
def test_set_equals(inp, expected):
    if not hasattr(list, "set_equals"):
        pytest.skip("set_equals() not implemented yet")
    assert list.set_equals(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["intersection"])
def test_intersection(inp, expected):
    if not hasattr(list, "intersection"):
        pytest.skip("intersection() not implemented yet")
    assert list.intersection(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["sum"])
def test_sum(inp, expected):
    if not hasattr(list, "sum"):
        pytest.skip("sum() not implemented yet")
    assert list.sum(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["max"])
def test_max(inp, expected):
    if not hasattr(list, "max"):
        pytest.skip("max() not implemented yet")
    assert list.max(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["smaller_than"])
def test_smaller_than(inp, expected):
    if not hasattr(list, "smaller_than"):
        pytest.skip("smaller_than() not implemented yet")
    assert list.smaller_than(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["two_zeros"])
def test_two_zeros(inp, expected):
    if not hasattr(list, "two_zeros"):
        pytest.skip("two_zeros() not implemented yet")
    assert list.two_zeros(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["even_after_7"])
def test_even_after_7(inp, expected):
    if not hasattr(list, "even_after_7"):
        pytest.skip("even_after_7() not implemented yet")
    assert list.even_after_7(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["is_sorted"])
def test_is_sorted(inp, expected):
    if not hasattr(list, "is_sorted"):
        pytest.skip("is_sorted() not implemented yet")
    assert list.is_sorted(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["squares"])
def test_squares(inp, expected):
    if not hasattr(list, "squares"):
        pytest.skip("squares() not implemented yet")
    assert list.squares(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["decreasing_squares"])
def test_deacreasing_squares(inp, expected):
    if not hasattr(list, "decreasing_squares"):
        pytest.skip("decreasing_squares() not implemented yet")
    assert list.decreasing_squares(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["divisors"])
def test_divisors(inp, expected):
    if not hasattr(list, "divisors"):
        pytest.skip("divisors() not implemented yet")
    assert list.divisors(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["square_it"])
def test_square_it(inp, expected):
    if not hasattr(list, "square_it"):
        pytest.skip("square_it() not implemented yet")
    assert list.square_it(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["reverse"])
def test_reverse(inp, expected):
    if not hasattr(list, "reverse"):
        pytest.skip("reverse() not implemented yet")
    assert list.reverse(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["compare"])
def test_compare(inp, expected):
    expected = tuple(expected)  # convert JSON array to tuple
    if not hasattr(list, "compare"):
        pytest.skip("compare() not implemented yet")
    assert list.compare(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["join"])
def test_join(inp, expected):
    if not hasattr(list, "join"):
        pytest.skip("join() not implemented yet")
    assert list.join(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["sorted_join"])
def test_sorted_join(inp, expected):
    if not hasattr(list, "sorted_join"):
        pytest.skip("sorted_join() not implemented yet")
    assert list.sorted_join(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["shuffle"])
def test_shuffle(inp, expected):
    if not hasattr(list, "shuffle"):
        pytest.skip("shuffle() not implemented yet")
    assert list.shuffle(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["remove"])
def test_remove(inp, expected):
    if not hasattr(list, "remove"):
        pytest.skip("remove() not implemented yet")
    assert list.remove(*inp) == expected