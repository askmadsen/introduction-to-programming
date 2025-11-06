from typing import List
from functools import reduce

# Functional programming
# Using the functions: reduce (built in), filter (built in), fixpoint, map (built in), iterate

def fixpoint(f, x):
    """ Applies f to x until the result does not change."""
    fx = f(x)
    if fx == x:
        return x
    else:
        return fixpoint(f, fx)

def iterate(f, x, n: int):
    """ Applies f to x a given number n>=0 of times."""
    if n == 0:
        return x
    else:
        return iterate(f, f(x), n - 1)


def sum(v: List[int]) -> int:
    """ Returns the sum of all values in v.
    >>> sum([1,2,3])
    6
    """
    return reduce(lambda x,y: x + y, v, 0)


def lenght(v: list) -> int:
    """ Returns the lenght of v.
    >>> lenght([1,5,7])
    3
    """
    return reduce(lambda x,y: x + 1, v, 0)


def remove(x: any, v: list) -> list:
    """ Returns v without the ellement that are x.
    >>> remove(1, [0,1,2,3,1])
    [0, 2, 3]
    """
    return list(filter(lambda y: y != x, v))


def count_1(x: any, v: list) -> int:
    """ Returns the number of times x appear in v.
    >>> count_1(1, [1,2,1,3,1])
    3
    """
    return sum(map(lambda y: 1 if x == y else 0, v))

def count_2(x: any, v: list) -> int:
    """ Returns the number of times x appear in v.
    >>> count_2(1, [1,2,1,3,1])
    3
    """
    return len(list(filter(lambda y: y == x, v)))

def count_3(x: any, v: list) -> int:
    """ Returns the number of times x appear in v.
    >>> count_3(1, [1,2,1,3,1])
    3
    """
    return reduce(lambda y,z: y + 1 if z == x else y, v, 0)


def max(v: list[int]) -> int:
    """ Returns the largest element in v.
    >>> max([2,3,1])
    3
    """
    return reduce(lambda x,y: x if x >= y else y, v, 0)


def square_it(v: List[int]) -> List[int]:
    """ Returns a list containing all squares of the elements of v.
    >>> square_it([1,2,3])
    [1, 4, 9]
    """
    return list(map(lambda x: x * x, v))


def squares(n: int) -> List[int]:
    """ Returns a list with the squares from 1 to n.
    >>> squares(4)
    [1, 4, 9, 16]
    """
    return square_it(range(1, n + 1))


def decreasing_squares(n: int) -> List[int]:
    """ Returns a list with the sqaures form n to 1.
    >>> decreasing_squares(3)
    [9, 4, 1]
    """
    return square_it(range(n, 0, -1))


def reverse(v: list) -> list:
    """ Reverses v.
    >>> reverse([1,2,3])
    [3, 2, 1]
    """
    return list(map(lambda x,y: y, v, v[::-1]))


def sum_up_to(n: int) -> int:
    """ Returns the sum of numbers up to n.
    >>> sum_up_to(5)
    15
    """
    return reduce(lambda x,y: x + y, range(1, n + 1), 0)


def sum_between(m: int, n: int) -> int:
    """ Returns the sum between m and n.
    >>> sum_between(2,5)
    14
    """
    return reduce(lambda x,y: x + y, range(m, n + 1), 0)


def sum_even(n: int) -> int:
    """ Returns the sum of even numbers up to n.
    >>> sum_even(6)
    12
    """
    return reduce(lambda x,y: x + y, range(0, n + 1, 2), 0)


def factorial(n: int) -> int:
    """ Returns the factorial of n.
    >>> factorial(5)
    120
    """
    return reduce(lambda x,y: x * y, range(1, n + 1), 1)


def double_factorial(n: int) -> int:
    """ Returns 1*3*...*n if n is odd and 2*4*...*n if n is even.
    >>> double_factorial(5)
    15
    >>> double_factorial(6)
    48
    """
    return reduce(lambda x,y: x * y, range(n, 0, -2), 1)


def member_1(x: any, v: list) -> bool:
    """ Checks wether x appears in v.
    >>> member_1(1, [0,1,2])
    True
    >>> member_1(1, [0,2,3])
    False
    """
    return list(filter(lambda y: y == x, v)) != []

def member_2(x: any, v: list) -> bool:
    """ Checks wether x appears in v.
    >>> member_2(1, [0,1,2])
    True
    >>> member_2(1, [0,2,3])
    False
    """
    return reduce(lambda y,z: y or x == z, v, False)


def subset(v: list, w: list) -> bool:
    """ Checks if all the elements in v occur in w.
    >>> subset([1,2,3], [1,2,3,4])
    True
    >>> subset([2,4], [1,2,3,5])
    False
    """
    return reduce(lambda x,y: x and member_1(y, w), v, True)


def intersection(v: list, w: list) -> list:
    """
    
    """
    return list(filter(lambda x: member_1(x, w), v))


def smaller_than(n: int, v: list[int]) -> int:
    """ Counts the number of elements in v strictly smaller than n.
    >>> smaller_than(2, [1,0,1,2,3])
    3
    """
    return reduce(lambda x,y: x + 1 if y < n else x, v, 0)


def caesar_code(s: str, n: int) -> str:
    """ Increases the ASCII cide of each element in s by n.
    >>> caesar_code('abc', 1)
    'bcd'
    """
    return reduce(lambda x,y: x + y,
                  map(lambda y: chr(ord(y) + n),s),
                  '')


def to_uppercase(s: str) -> str:
    """ Converts s to uppercase.
    >>> to_uppercase('abc')
    'ABC'
    """
    return reduce(lambda x,y: x + y,
                  map(lambda x: chr(ord(x) - 32) if 97 <= ord(x) <= 122 else x, s),
                  '')


def to_lowercase(s: str) -> str:
    """ Converts s to lowercase.
    >>> to_lowercase('ABC')
    'abc'
    """
    return reduce(lambda x,y: x + y,
                  map(lambda x: chr(ord(x) + 32) if 65 <= ord(x) <= 90 else x, s),
                  '')

def count_divisors_1(n: int) -> int:
    """ Returns the number of divisors of n.
    >>> count_divisors_1(6)
    4
    >>> count_divisors_1(1)
    1
    """
    return reduce(lambda x,y: x + 1 if n % y == 0 else x, range(1, n + 1), 0)


def count_divisors_2(n: int) -> int:
    """ Returns the number of divisors of n.
    >>> count_divisors_2(6)
    4
    >>> count_divisors_2(1)
    1
    """
    return reduce(lambda x,y: x + 1,
                  filter(lambda x: n % x == 0, range(1, n // 2 + 1)),
                  1)


def is_perfect(n: int) -> bool:
    """ Checks if n is a perfect number.
    >>> is_perfect(6)
    True
    >>> is_perfect(5)
    False
    """
    return reduce(lambda x,y: x + y,
                  filter(lambda x: n % x == 0, range(1, n // 2 + 1)),
                         0) == n


def count_perfect(n: int) -> int:
    """ Returns the number of perfect numbers smaller than n
    >>> count_perfect(28)
    1
    >>> count_perfect(29)
    2
    """
    return reduce(lambda x,y: x + 1 if is_perfect(y) else x, range(1, n), 0)


def is_prime(n: int) -> bool:
    """ Check if n is prime.
    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    """
    return reduce(lambda x,y: x and y,
                  map(lambda x: n % x != 0,
                      range(2, n // 2 + 1)),
                  n > 1)
    

def count_primes_1(n: int) -> int:
    """ Returns the number of primes smaller than n.
    >>> count_primes_1(2)
    0
    >>> count_primes_1(6)
    3
    """
    return reduce(lambda x,y: x + 1 if is_prime(y) else x, range(1, n),0)


def count_primes_2(n: int) -> int:
    """ Returns the number of primes smaller than n.
    >>> count_primes_2(2)
    0
    >>> count_primes_2(9)
    4
    """
    return reduce(lambda x,y: x + 1,
                  filter(is_prime, range(1, n)),
                  0)
    

def two_zeros_1(v: list[int]) -> bool:
    """ Checks if two zeros appear right after each other.
    >>> two_zeros_1([0,0,1])
    True
    >>> two_zeros_1([0,1,0])
    False
    """
    return reduce(lambda x,y: x or y,
                  map(lambda i: v[i] == v[i + 1] == 0,
                      range(len(v) - 1)),
                      False)


def two_zeros_2(v: list[int]) -> bool:
    """ Checks if two zeros appear right after each other.
    >>> two_zeros_2([0,0,1])
    True
    >>> two_zeros_2([0,1,0])
    False
    """
    return reduce(lambda x,y: x or y,
                  map(lambda x,y: x == y == 0,
                      v[1:],
                      v[:-1]),
                  False)


def is_sorted(v: list[int]) -> bool:
    """ Checks if v is sorted.
    >>> is_sorted([1,2,2,4])
    True
    >>> is_sorted([2,1,4])
    False
    """
    return reduce(lambda x,y: x and y,
                  map(lambda x,y: x >= y,
                      v[1:],
                      v[:-1]),
                  True)

def compare(v: list[int], n: int) -> (int, int, int):
    """ Returns a tuple containing the number of elements in v larger than, equal to or smallet than n.
    >>> compare([0,1,2,1,3,2], 2)
    (1, 2, 3)
    """
    return (len(list(filter(lambda x: x > n, v))),
            len(list(filter(lambda x: x == n, v))),
            len(list(filter(lambda x: x < n, v))))


def positions(c: str, s: str) -> list[int]:
    """ Returns a list with the indices of the occurences if c in v.
    >>> positions('a', 'banana')
    [1, 3, 5]
    """
    return list(filter(lambda x: x != -1,
                       map(lambda x,y: y if x == c else -1, s,
                           range(len(s)))))


def replicate(s: str, v: list[int]) -> str:
    """ Returns a string with v[i] copies of s[i] given that len(v) == len(s).
    >>> replicate('abc', [1,2,3])
    'abbccc'
    """
    return reduce(lambda x,y: x + y,
                  list(map(lambda x,y: x * y, v, s)),
                  '')


def remove_vowels(s: str) -> str:
    """ Returns s with all its vowels removed.
    >>> remove_vowels('abcde')
    'bcd'
    """
    return reduce(lambda x,y: x + y,
                  list(filter(lambda x: not member_1(x, 'aAeEiIoOuUyY'), s)),
                  '')


def encode_with_key(s: str, code: dict[str, str]) -> str:
    """ Maps uppercase letters to its encoding.
    >>> encode_with_key('HEJ', {'H' : 't', 'E' : 'o', 'J' : 'p'})
    'top'
    """
    return reduce(lambda x,y: x + y,
                  list(map(lambda x: code[x], s)),
                  '')