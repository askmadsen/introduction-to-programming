# Imperative programming on numbers

def print_multiples(k: int, n: int) -> None:
    """ Prints the multiples of k less than n.
    """
    multiple = k
    while multiple <= n:
        print(multiple)
        multiple = multiple + k


def sum_up_to(n: int) -> int:
    """ Returns the sum of natural numbers up to n.
    >>> sum_up_to(10)
    55
    """
    sum = 0
    i = 1
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum


def sum_even(n: int) -> int:
    """ Returns the sum of even natural numbers up to n.
    >>> sum_even(1)
    0
    >>> sum_even(7)
    12
    """
    sum = 0
    i = 2
    while i <= n:
        sum = sum + i
        i = i + 2
    return sum


def sum_between(m: int, n: int) -> int:
    """ Returns the sum of numbers between m and n.
    >>> sum_between(3,5)
    12
    """
    sum = 0
    i = m
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum


def sum_beyond(k: int) -> int:
    """ Returns the least n such that sum_up_to(n) is at least k.
    >>> sum_beyond(49)
    10
    """
    i = 0
    sum = 0
    while sum < k:
        i = i + 1
        sum = sum + i
    return i


def factorial(n: int) -> int:
    """ Returns the factorial of n.
    >>> factorial(5)
    120
    """
    fact = 1
    i = 2
    while i <= n:
        fact = fact * i
        i = i + 1
    return fact


def double_factorial(n: int) -> int:
    """ Returns the double factorial of n.
    >>> double_factorial(5)
    15
    >>> double_factorial(6)
    48
    """
    fact = 1
    i = 2
    while i <= n:
        if n % 2 == 0:
            fact = fact * i
        else:
            fact = fact * (i + 1)
        i = i + 2
    return fact


def fibonacci(n: int) -> int:
    """ Returns the nth fibonacci number.
    >>> fibonacci(5)
    8
    """
    prev = 1
    next = 1
    i = 1
    while i < n:
        sum = prev + next
        prev = next
        next = sum
        i = i + 1
    return next


def logarithm(n: int, m: int = 2) -> int:
    """ Returns the integer base-m logarithm of n.
    >>> logarithm(8)
    3
    >>> logarithm(27, 5)
    2
    """
    power = 1
    i = 0
    while power <= n:
        i = i + 1
        power = power * m
    return i - 1


def count_divisors(n: int) -> int:
    """ Returns the number of divisors n has.
    >>> count_divisors(12)
    6
    """
    divisors = 1
    i = 1
    while i <= (n // 2 + 1):
        if n % i == 0:
            divisors = divisors + 1
        i = i + 1
    return divisors


def is_perfect(n: int) -> bool:
    """ Checks wether n is a perfect number.
    >>> is_perfect(6)
    True
    >>> is_perfect(7)
    False
    """
    sum = 0
    i = 1
    while i <= n - 1:
        if n % i == 0:
            sum = sum + i
        i = i + 1
    return sum == n


def count_perfect(n: int) -> int:
    """ Returns the number if perfect numbers smaller than n.
    >>> count_perfect(7)
    1
    >>> count_perfect(29)
    2
    """
    count = 0
    i = 1
    while i <= n - 1:
        if is_perfect(i):
            count = count + 1
        i = i + 1
    return count


def is_prime(n: int) -> bool:
    """ Checks if n is prime.
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    """
    divisor = 0
    i = 1
    while i <= n:
        if n % i == 0:
            divisor = divisor + 1
        i = i + 1
    return divisor == 2
            

def count_primes(n: int) -> int:
    """ Returns the number of primes smaller than n.
    >>> count_primes(3)
    1
    >>> count_primes(12)
    5
    """
    count = 0
    i = 1
    while i < n:
        if is_prime(i):
            count = count + 1
        i = i + 1
    return count


def nth_prime(n: int) -> int:
    """ Returns the nth prime number.
    >>> nth_prime(5)
    11
    """
    i = 1
    prime = 0
    while prime < n:
        if is_prime(i):
            prime = prime + 1
        i = i + 1
    return i - 1


def gcd(m: int, n: int) -> int:
    """ Returns the greatest common divisor of m and n.
    >>> gcd(4, 14)
    2
    """
    while m != n:
        if m < n:
            n = n - m
        else:
            m = m - n
    return m