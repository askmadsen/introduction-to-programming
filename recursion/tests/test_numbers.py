import json
import pytest
import recursion.numbers as numbers 

with open("recursion/tests/test_numbers_cases.json") as f:
    cases = json.load(f)

@pytest.mark.parametrize("inp,expected", cases["sum_up_to"])
def test_sum_up_to(inp, expected):
    if not hasattr(numbers, "sum_up_to"):
        pytest.skip("sum_up_to() not implemented yet")
    assert numbers.sum_up_to(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["sum_even"])
def test_sum_even(inp, expected):
    if not hasattr(numbers, "sum_even"):
        pytest.skip("sum_even() not implemented yet")
    assert numbers.sum_even(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["sum_between"])
def test_sum_between(inp, expected):
    if not hasattr(numbers, "sum_between"):
        pytest.skip("sum_between() not implemented yet")
    assert numbers.sum_between(*inp) == expected # Unpacks the list of arguments inp using *

@pytest.mark.parametrize("inp,expected", cases["factorial"])
def test_factorial(inp, expected):
    if not hasattr(numbers, "factorial"):
        pytest.skip("factorial() not implemented yet")
    assert numbers.factorial(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["double_factorial"])
def test_double_factorial(inp, expected):
    if not hasattr(numbers, "double_factorial"):
        pytest.skip("double_factorial() not implemented yet")
    assert numbers.double_factorial(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["logarithm"])
def test_logarithm(inp, expected):
    if not hasattr(numbers, "logarithm"):
        pytest.skip("logarithm() not implemented yet")
    assert numbers.logarithm(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["gcd"])
def test_gcd(inp, expected):
    if not hasattr(numbers, "gcd"):
        pytest.skip("gcd() not implemented yet")
    assert numbers.gcd(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["lcm"])
def test_lcm(inp, expected):
    if not hasattr(numbers, "lcm"):
        pytest.skip("lcm() not implemented yet")
    assert numbers.lcm(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["first_digit"])
def test_first_digit(inp, expected):
    if not hasattr(numbers, "first_digit"):
        pytest.skip("first_digit() not implemented yet")
    assert numbers.first_digit(*inp) == expected

@pytest.mark.parametrize("inp,expected", cases["count_divisors"])
def test_count_divisors(inp, expected):
    if not hasattr(numbers, "count_divisors"):
        pytest.skip("count_divisors() not implemented yet")
    assert numbers.count_divisors(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["is_perfect"])
def test_is_perfect(inp, expected):
    if not hasattr(numbers, "is_perfect"):
        pytest.skip("is_perfect() not implemented yet")
    assert numbers.is_perfect(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["count_perfect"])
def test_count_perfect(inp, expected):
    if not hasattr(numbers, "count_perfect"):
        pytest.skip("count_perfect() not implemented yet")
    assert numbers.count_perfect(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["is_prime"])
def test_is_prime(inp, expected):
    if not hasattr(numbers, "is_prime"):
        pytest.skip("is_prime() not implemented yet")
    assert numbers.is_prime(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["count_primes"])
def test_count_primes(inp, expected):
    if not hasattr(numbers, "count_primes"):
        pytest.skip("count_primes() not implemented yet")
    assert numbers.count_primes(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["sum_beyond"])
def test_sum_beyond(inp, expected):
    if not hasattr(numbers, "sum_beyond"):
        pytest.skip("sum_beyond() not implemented yet")
    assert numbers.sum_beyond(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["is_palindrome"])
def test_is_palindrome(inp, expected):
    if not hasattr(numbers, "is_palindrome"):
        pytest.skip("is_palindrome() not implemented yet")
    assert numbers.is_palindrome(inp) == expected

@pytest.mark.parametrize("inp,expected", cases["find_power"])
def test_find_power(inp, expected):
    if not hasattr(numbers, "find_power"):
        pytest.skip("find_power() not implemented yet")
    assert numbers.find_power(inp) == expected