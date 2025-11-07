# 2 Recursive programming with numbers

def sum_up_to(n: int) -> int:
    """Returns the sum of natural numbers up to n."""
    if n <= 0:
        return 0
    else:
        return n + sum_up_to(n-1)

def sum_even(n: int) -> int:
    """Returns the sum of even natural numbers up to n."""
    if n <= 0: #allows n < 0
        return 0
    elif n % 2 == 0:
        return n + sum_even(n - 2)
    else:
        return sum_even(n - 1)

def sum_between(m: int, n: int) -> int:
    """Returns the sum of natural numbers between m and n."""
    if n < m:
        return 0
    else:
        return m + sum_between(m + 1, n)

def factorial(n: int) -> int:
    """Returns the factorial of n. Precondition: n >= 0."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def double_factorial(n: int) -> int:
    """Returns the factorial of odd or even numbers if n is odd or even. Precondition: n >= 0."""
    if n <= 0:
        return 1
    elif n > 0:
        return n * double_factorial(n - 2)
   
def logarithm(n: int) -> int:
    """Return the integer base 2 logarithm of n."""
    if n == 1:
        return 0
    else:
        return 1 + logarithm(n // 2)

def gcd(m: int, n: int) -> int:
    """Returns the greatest common divisor of m and n. Precondition: m,n > 0."""
    if m == n:
        return m
    elif m < n:
        return gcd(m, n - m)
    else:
        return gcd(m - n, n)

def lcm(m: int, n: int) -> int:
    """Returns the least common multiple of m and n. Precondition: m,n > 0."""
    return (m * n) // gcd(m,n)

def first_digit(n: int, k: int = 10) -> int:
    """Returns the first digit of the decimal representation of n in base k. Precondition: n,k > 0."""
    if n < k:
        return n
    else:
        return first_digit(n // k, k)

def print_multiples(k: int, n: int) -> None:
    """Prints the multiples of n less than k."""
    return _print_multiples(k, k, n)

def _print_multiples(start: int, step: int, end: int) -> None:
    if start < end:
        print(start)
        _print_multiples(start + step, step, end)

def count_divisors(n: int) -> int:
    """Returns the number of divisors of n. Precondition: n > 0."""
    return _count_divisors(n)

def _count_divisors(n: int, i: int = 1) -> int:
        if n == i:
            return 1
        elif n % i == 0:
            return 1 + _count_divisors(n, i + 1)
        else:
            return _count_divisors(n, i + 1)

def is_perfect(n: int) -> bool:
    """ Checks if n os a perfect number or not."""
    return n == _is_perfect(n)

def _is_perfect(n: int, i: int = 1) -> int:
    if n == i:
        return 0
    elif n % i == 0:
        return i + _is_perfect(n, i + 1)
    else:
        return _is_perfect(n, i + 1)

def count_perfect(n: int) -> int:
    """ Returns the number of perfect numbers smaller than n."""
    return _count_perfect(n)

def _count_perfect(n: int, i: int = 1) -> int:
    if n == i:
        return 0
    elif is_perfect(i):
        return 1 + _count_perfect(n, i + 1)
    else:
        return _count_perfect(n, i + 1)

def is_prime(n: int) -> bool:
    """ Checks if n is a prime number."""
    if n == 2:
        return True
    elif count_divisors(n) == 2:
        return True
    else:
        return False

def count_primes(n: int) -> int:
    """Returns the number of primes smaller than n."""
    return _count_primes(n)

def _count_primes(n: int, i: int = 1) -> int:
    if n <= i:
        return 0
    elif is_prime(i):
        return 1 + _count_primes(n, i + 1)
    else:
        return _count_primes(n, i + 1)

def sum_beyond(k: int) -> int:
    """ Returns the least n such that the sum of numbers up to n is at least k."""
    return _sum_beyond(k)

def _sum_beyond(k: int, i: int = 1) -> int:
    if sum_up_to(i) < k:
        return _sum_beyond(k, i + 1)
    else:
        return i

def is_palindrome(n: int) -> bool:
    """ Checks if n is a palindrome."""
    n1 = int(str(n)[::-1]) # converts n to string and inverts
    return n1 == n

def find_power(k: int) -> int:
    """ Returns the smallest number n such that 2 raised to the power n starts with k."""
    if k == 1:
        return 0
    return _find_power(k)

def _find_power(k: int, n: int = 1) -> int:
    if int(str(2 ** n)[0]) == k:
        return n
    else:
        return _find_power(k, n + 1)