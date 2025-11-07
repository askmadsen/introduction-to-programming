import json
import pytest
import recursion.strings as string

with open("recursion/tests/test_strings_cases.json") as f:
    cases = json.load(f)

@pytest.mark.parametrize("inp,expected", cases["count"])
def test_count(inp, expected):
    if not hasattr(string, "count"):
        pytest.skip("count() not implemented yet")
    assert string.count(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["member"])
def test_member(inp, expected):
    if not hasattr(string, "member"):
        pytest.skip("member() not implemented yet")
    assert string.member(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["is_prefix"])
def test_is_prefix(inp, expected):
    if not hasattr(string, "is_prefix"):
        pytest.skip("is_prefix() not implemented yet")
    assert string.is_prefix(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["is_suffix"])
def test_is_suffix(inp, expected):
    if not hasattr(string, "is_suffix"):
        pytest.skip("is_suffix() not implemented yet")
    assert string.is_suffix(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["is_substring"])
def test_is_substring(inp, expected):
    if not hasattr(string, "is_substring"):
        pytest.skip("is_substring() not implemented yet")
    assert string.is_substring(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["contains"])
def test_contains(inp, expected):
    if not hasattr(string, "contains"):
        pytest.skip("contains() not implemented yet")
    assert string.contains(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["caesar_code"])
def test_caesar_code(inp, expected):
    if not hasattr(string, "caesar_code"):
        pytest.skip("caesar_code() not implemented yet")
    assert string.caesar_code(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["to_uppercase"])
def test_to_uppercase(inp, expected):
    if not hasattr(string, "to_uppercase"):
        pytest.skip("to_uppercase() not implemented yet")
    assert string.to_uppercase(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["to_lowercase"])
def test_to_lowercase(inp, expected):
    if not hasattr(string, "to_lowercase"):
        pytest.skip("to_lowercase() not implemented yet")
    assert string.to_lowercase(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["toCamelCase"])
def test_toCamelCase(inp, expected):
    if not hasattr(string, "toCamelCase"):
        pytest.skip("toCamelCase() not implemented yet")
    assert string.toCamelCase(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["equals_ignore_case"])
def test_equals_ignore_case(inp, expected):
    if not hasattr(string, "equals_ignore_case"):
        pytest.skip("equals_ignore_case() not implemented yet")
    assert string.equals_ignore_case(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["first_position"])
def test_first_position(inp, expected):
    if not hasattr(string, "first_position"):
        pytest.skip("first_position() not implemented yet")
    assert string.first_position(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["last_position"])
def test_last_position(inp, expected):
    if not hasattr(string, "last_position"):
        pytest.skip("last_position() not implemented yet")
    assert string.last_position(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["positions"])
def test_positions(inp, expected):
    if not hasattr(string, "positions"):
        pytest.skip("positions() not implemented yet")
    assert string.positions(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["is_permutation"])
def test_is_permutation(inp, expected):
    if not hasattr(string, "is_permutation"):
        pytest.skip("is_permutation() not implemented yet")
    assert string.is_permutation(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["reverse"])
def test_reverse(inp, expected):
    if not hasattr(string, "reverse"):
        pytest.skip("reverse() not implemented yet")
    assert string.reverse(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["reverse_words"])
def test_reverse_words(inp, expected):
    if not hasattr(string, "reverse_words"):
        pytest.skip("reverse_words() not implemented yet")
    assert string.reverse_words(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["remove_vowels"])
def test_remove_vowels(inp, expected):
    if not hasattr(string, "reverse_words"):
        pytest.skip("remove_vowels() not implemented yet")
    assert string.remove_vowels(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["respace"])
def test_respace(inp, expected):
    if not hasattr(string, "respace"):
        pytest.skip("respace() not implemented yet")
    assert string.respace(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["encode_with_key"])
def test_encode_with_key(inp, expected):
    if not hasattr(string, "encode_with_key"):
        pytest.skip("encode_with_key() not implemented yet")
    assert string.encode_with_key(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["histogram"])
def test_histogram(inp, expected):
    if not hasattr(string, "histogram"):
        pytest.skip("histogram() not implemented yet")
    assert string.histogram(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["replicate"])
def test_replicate(inp, expected):
    if not hasattr(string, "replicate"):
        pytest.skip("replicate() not implemented yet")
    assert string.replicate(*inp) == expected