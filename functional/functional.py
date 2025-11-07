from functools import reduce

# 5 Functional programming

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

def sum(v: list[int]) -> int:
    """ Returns the sum of all values in v."""
    return reduce(lambda x,y: x + y, v, 0)

def length(v: list) -> int:
    """ Returns the lenght of v."""
    return reduce(lambda x,y: x + 1, v, 0)

def remove(x: any, v: list) -> list:
    """ Returns v without the ellement that are x."""
    return list(filter(lambda y: y != x, v))

def count_1(x: any, v: list) -> int:
    """ Returns the number of times x appear in v."""
    return sum(map(lambda y: 1 if x == y else 0, v))

def count_2(x: any, v: list) -> int:
    """ Returns the number of times x appear in v."""
    return len(list(filter(lambda y: y == x, v)))

def count_3(x: any, v: list) -> int:
    """ Returns the number of times x appear in v."""
    return reduce(lambda y,z: y + 1 if z == x else y, v, 0)

def max(v: list[int]) -> int:
    """ Returns the largest element in v."""
    return reduce(lambda x,y: x if x >= y else y, v)

def square_it(v: list[int]) -> list[int]:
    """ Returns a list containing all squares of the elements of v."""
    return list(map(lambda x: x * x, v))

def squares(n: int) -> list[int]:
    """ Returns a list with the squares from 1 to n."""
    return square_it(range(1, n + 1))

def decreasing_squares(n: int) -> list[int]:
    """ Returns a list with the sqaures form n to 1."""
    return square_it(range(n, 0, -1))

def reverse(v: list) -> list:
    """ Reverses v."""
    return list(map(lambda x,y: y, v, v[::-1]))

def sum_up_to(n: int) -> int:
    """ Returns the sum of numbers up to n."""
    return reduce(lambda x,y: x + y, range(1, n + 1), 0)

def sum_between(m: int, n: int) -> int:
    """ Returns the sum between m and n."""
    return reduce(lambda x,y: x + y, range(m, n + 1), 0)

def sum_even(n: int) -> int:
    """ Returns the sum of even numbers up to n."""
    return reduce(lambda x,y: x + y, range(0, n + 1, 2), 0)

def factorial(n: int) -> int:
    """ Returns the factorial of n."""
    return reduce(lambda x,y: x * y, range(1, n + 1), 1)

def double_factorial(n: int) -> int:
    """ Returns 1*3*...*n if n is odd and 2*4*...*n if n is even."""
    return reduce(lambda x,y: x * y, range(n, 0, -2), 1)

def member_1(x: any, v: list) -> bool:
    """ Checks wether x appears in v."""
    return list(filter(lambda y: y == x, v)) != []

def member_2(x: any, v: list) -> bool:
    """ Checks wether x appears in v."""
    return reduce(lambda y,z: y or x == z, v, False)

def subset(v: list, w: list) -> bool:
    """ Checks if all the elements in v occur in w."""
    return reduce(lambda x,y: x and member_1(y, w), v, True)

def intersection(v: list, w: list) -> list:
    """ Returns a list of the elements that occur both in v and w."""
    return list(filter(lambda x: member_1(x, w), v))

def smaller_than(n: int, v: list[int]) -> int:
    """ Counts the number of elements in v strictly smaller than n."""
    return reduce(lambda x,y: x + 1 if y < n else x, v, 0)

def caesar_code(s: str, n: int) -> str:
    """ Increases the ASCII code of each element in s by n."""
    return reduce(lambda x,y: x + y,
                  map(lambda y: chr(ord(y) + n),s),
                  '')

def to_uppercase(s: str) -> str:
    """ Converts s to uppercase."""
    return reduce(lambda x,y: x + y,
                  map(lambda x: chr(ord(x) - 32) if 97 <= ord(x) <= 122 else x, s),
                  '')

def to_lowercase(s: str) -> str:
    """ Converts s to lowercase."""
    return reduce(lambda x,y: x + y,
                  map(lambda x: chr(ord(x) + 32) if 65 <= ord(x) <= 90 else x, s),
                  '')

def count_divisors_1(n: int) -> int:
    """ Returns the number of divisors of n."""
    return reduce(lambda x,y: x + 1 if n % y == 0 else x, range(1, n + 1), 0)

def count_divisors_2(n: int) -> int:
    """ Returns the number of divisors of n."""
    return reduce(lambda x,y: x + 1,
                  filter(lambda x: n % x == 0, range(1, n // 2 + 1)),
                  1)

def is_perfect(n: int) -> bool:
    """ Checks if n is a perfect number."""
    return reduce(lambda x,y: x + y,
                  filter(lambda x: n % x == 0, range(1, n // 2 + 1)),
                         0) == n

def count_perfect(n: int) -> int:
    """ Returns the number of perfect numbers smaller than n."""
    return reduce(lambda x,y: x + 1 if is_perfect(y) else x, range(1, n), 0)

def is_prime(n: int) -> bool:
    """ Check if n is prime."""
    return reduce(lambda x,y: x and y,
                  map(lambda x: n % x != 0,
                      range(2, n // 2 + 1)),
                  n > 1)
    
def count_primes_1(n: int) -> int:
    """ Returns the number of primes smaller than n."""
    return reduce(lambda x,y: x + 1 if is_prime(y) else x, range(1, n),0)

def count_primes_2(n: int) -> int:
    """ Returns the number of primes smaller than n."""
    return reduce(lambda x,y: x + 1,
                  filter(is_prime, range(1, n)),
                  0)
    
def two_zeros_1(v: list[int]) -> bool:
    """ Checks if two zeros appear right after each other."""
    return reduce(lambda x,y: x or y,
                  map(lambda i: v[i] == v[i + 1] == 0,
                      range(len(v) - 1)),
                      False)

def two_zeros_2(v: list[int]) -> bool:
    """ Checks if two zeros appear right after each other."""
    return reduce(lambda x,y: x or y,
                  map(lambda x,y: x == y == 0,
                      v[1:],
                      v[:-1]),
                  False)

def is_sorted(v: list[int]) -> bool:
    """ Checks if v is sorted."""
    return reduce(lambda x,y: x and y,
                  map(lambda x,y: x >= y,
                      v[1:],
                      v[:-1]),
                  True)

def compare(v: list[int], n: int) -> tuple[int, int, int]:
    """ Returns a tuple containing the number of elements in v larger than, equal to or smallet than n."""
    return (len(list(filter(lambda x: x > n, v))),
            len(list(filter(lambda x: x == n, v))),
            len(list(filter(lambda x: x < n, v))))

def positions(c: str, s: str) -> list[int]:
    """ Returns a list with the indices of the occurences if c in v."""
    return list(filter(lambda x: x != -1,
                       map(lambda x,y: y if x == c else -1, s,
                           range(len(s)))))

def replicate(s: str, v: list[int]) -> str:
    """ Returns a string with v[i] copies of s[i] given that len(v) == len(s)."""
    return reduce(lambda x,y: x + y,
                  list(map(lambda x,y: x * y, v, s)),
                  '')

def remove_vowels(s: str) -> str:
    """ Returns s with all its vowels removed."""
    return reduce(lambda x,y: x + y,
                  list(filter(lambda x: not member_1(x, 'aAeEiIoOuUyY'), s)),
                  '')

def encode_with_key(s: str, code: dict[str, str]) -> str:
    """ Maps uppercase letters to its encoding."""
    return reduce(lambda x,y: x + y,
                  list(map(lambda x: code.get(to_uppercase(x), x), s)),
                  '')