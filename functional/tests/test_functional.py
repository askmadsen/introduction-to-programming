import json
import pytest
import functional.functional as func

with open("functional/tests/test_functional_cases.json") as f:
    cases = json.load(f)

@pytest.mark.parametrize("inp,expected", cases["sum"])
def test_sum(inp, expected):
    if not hasattr(func, "sum"):
        pytest.skip("sum() not implemented yet")
    assert func.sum(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["length"])
def test_length(inp, expected):
    if not hasattr(func, "length"):
        pytest.skip("length() not implemented yet")
    assert func.length(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["remove"])
def test_remove(inp, expected):
    if not hasattr(func, "remove"):
        pytest.skip("remove() not implemented yet")
    assert func.remove(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["count_3"])
def test_count_3(inp, expected):
    if not hasattr(func, "count_3"):
        pytest.skip("count_3() not implemented yet")
    assert func.count_3(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["max"])
def test_max(inp, expected):
    if not hasattr(func, "max"):
        pytest.skip("max() not implemented yet")
    assert func.max(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["square_it"])
def test_square_it(inp, expected):
    if not hasattr(func, "square_it"):
        pytest.skip("square_it() not implemented yet")
    assert func.square_it(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["squares"])
def test_squares(inp, expected):
    if not hasattr(func, "squares"):
        pytest.skip("squares() not implemented yet")
    assert func.squares(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["decreasing_squares"])
def test_decreasing_squares(inp, expected):
    if not hasattr(func, "decreasing_squares"):
        pytest.skip("decreasing_squares() not implemented yet")
    assert func.decreasing_squares(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["reverse"])
def test_reverse(inp, expected):
    if not hasattr(func, "reverse"):
        pytest.skip("reverse() not implemented yet")
    assert func.reverse(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["sum_up_to"])
def test_sum_up_to(inp, expected):
    if not hasattr(func, "sum_up_to"):
        pytest.skip("sum_up_to() not implemented yet")
    assert func.sum_up_to(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["sum_between"])
def test_sum_between(inp, expected):
    if not hasattr(func, "sum_between"):
        pytest.skip("sum_between() not implemented yet")
    assert func.sum_between(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["sum_even"])
def test_sum_even(inp, expected):
    if not hasattr(func, "sum_even"):
        pytest.skip("sum_even() not implemented yet")
    assert func.sum_even(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["factorial"])
def test_factorial(inp, expected):
    if not hasattr(func, "factorial"):
        pytest.skip("factorial() not implemented yet")
    assert func.factorial(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["double_factorial"])
def test_double_factorial(inp, expected):
    if not hasattr(func, "double_factorial"):
        pytest.skip("double_factorial() not implemented yet")
    assert func.double_factorial(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["member_2"])
def test_member_2(inp, expected):
    if not hasattr(func, "member_2"):
        pytest.skip("member_2() not implemented yet")
    assert func.member_2(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["subset"])
def test_subset(inp, expected):
    if not hasattr(func, "subset"):
        pytest.skip("subset() not implemented yet")
    assert func.subset(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["intersection"])
def test_intersection(inp, expected):
    if not hasattr(func, "intersection"):
        pytest.skip("intersection() not implemented yet")
    assert func.intersection(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["smaller_than"])
def test_smaller_than(inp, expected):
    if not hasattr(func, "smaller_than"):
        pytest.skip("smaller_than() not implemented yet")
    assert func.smaller_than(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["caesar_code"])
def test_caesar_code(inp, expected):
    if not hasattr(func, "caesar_code"):
        pytest.skip("caesar_code() not implemented yet")
    assert func.caesar_code(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["to_uppercase"])
def test_to_uppercase(inp, expected):
    if not hasattr(func, "to_uppercase"):
        pytest.skip("to_uppercase() not implemented yet")
    assert func.to_uppercase(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["to_lowercase"])
def test_to_lowercase(inp, expected):
    if not hasattr(func, "to_lowercase"):
        pytest.skip("to_lowercase() not implemented yet")
    assert func.to_lowercase(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["count_divisors_1"])
def test_count_divisors_1(inp, expected):
    if not hasattr(func, "count_divisors_1"):
        pytest.skip("count_divisors_1() not implemented yet")
    assert func.count_divisors_1(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["is_perfect"])
def test_is_perfect(inp, expected):
    if not hasattr(func, "is_perfect"):
        pytest.skip("is_perfect() not implemented yet")
    assert func.is_perfect(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["count_perfect"])
def test_count_perfect(inp, expected):
    if not hasattr(func, "count_perfect"):
        pytest.skip("count_perfect() not implemented yet")
    assert func.count_perfect(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["is_prime"])
def test_is_prime(inp, expected):
    if not hasattr(func, "is_prime"):
        pytest.skip("is_prime() not implemented yet")
    assert func.is_prime(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["count_primes_1"])
def test_count_primes_1(inp, expected):
    if not hasattr(func, "count_primes_1"):
        pytest.skip("count_primes_1() not implemented yet")
    assert func.count_primes_1(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["two_zeros_2"])
def test_two_zeros_2(inp, expected):
    if not hasattr(func, "two_zeros_2"):
        pytest.skip("two_zeros_2() not implemented yet")
    assert func.two_zeros_2(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["is_sorted"])
def test_is_sorted(inp, expected):
    if not hasattr(func, "is_sorted"):
        pytest.skip("is_sorted() not implemented yet")
    assert func.is_sorted(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["compare"])
def test_compare(inp, expected):
    expected = tuple(expected)
    if not hasattr(func, "compare"):
        pytest.skip("compare() not implemented yet")
    assert func.compare(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["positions"])
def test_positions(inp, expected):
    if not hasattr(func, "positions"):
        pytest.skip("positions() not implemented yet")
    assert func.positions(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["replicate"])
def test_replicate(inp, expected):
    if not hasattr(func, "replicate"):
        pytest.skip("replicate() not implemented yet")
    assert func.replicate(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["remove_vowels"])
def test_remove_vowels(inp, expected):
    if not hasattr(func, "remove_vowels"):
        pytest.skip("remove_vowels() not implemented yet")
    assert func.remove_vowels(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["encode_with_key"])
def test_encode_with_key(inp, expected):
    if not hasattr(func, "encode_with_key"):
        pytest.skip("encode_with_key() not implemented yet")
    assert func.encode_with_key(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["gcd"])
def test_gcd(inp, expected):
    if not hasattr(func, "gcd"):
        pytest.skip("gcd() not implemented yet")
    assert func.gcd(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["first_digit"])
def test_first_digit(inp, expected):
    if not hasattr(func, "first_digit"):
        pytest.skip("first_digit() not implemented yet")
    assert func.first_digit(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["trim"])
def test_trim(inp, expected):
    if not hasattr(func, "trim"):
        pytest.skip("trim() not implemented yet")
    assert func.trim(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["dimensions"])
def test_dimensions(inp, expected):
    if not hasattr(func, "dimensions"):
        pytest.skip("dimensions() not implemented yet")
    assert func.dimensions(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["is_matrix"])
def test_is_matrix(inp, expected):
    if not hasattr(func, "is_matrix"):
        pytest.skip("is_matrix() not implemented yet")
    assert func.is_matrix(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["is_square_matrix"])
def test_is_square_matrix(inp, expected):
    if not hasattr(func, "is_square_matrix"):
        pytest.skip("is_square_matrix() not implemented yet")
    assert func.is_square_matrix(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["zeros"])
def test_zeros(inp, expected):
    if not hasattr(func, "zeros"):
        pytest.skip("zeros() not implemented yet")
    assert func.zeros(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["identity"])
def test_identity(inp, expected):
    if not hasattr(func, "identity"):
        pytest.skip("identity() not implemented yet")
    assert func.identity(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["triangle"])
def test_triangle(inp, expected):
    if not hasattr(func, "triangle"):
        pytest.skip("triangle() not implemented yet")
    assert func.triangle(inp) == expected