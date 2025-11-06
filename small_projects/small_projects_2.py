# Small projects

def eratosthenes(n: int) -> list[int]:
    """ Returns a list with the prime numbers smaller than or equal to n.
    >>> eratosthenes(12)
    [2, 3, 5, 7, 11]
    """
    primes = list(range(n+1))
    primes[1] = 0
    bound = n ** 0.5
    i = 2
    while i <= bound:
        if primes[i] != 0:
            j = i * 2
            while j <= n:
                primes[j] = 0
                j = j + i
        i = i + 1
    return [x for x in primes if x != 0]
            

def integral(f, a: float, b: float, n: int) -> float:
    """ Approximates the integral of f on the interval [a, b]."""
    area = 0
    step_size = (b - a) / n
    x = a + step_size / 2
    while x < b:
        area = area + step_size * f(x)
        x = x + step_size
    return area


def bisection(f, a: float, b: float, eps: float) -> float:
    """ Approximates the solution for f(x) = 0."""
    while b - a >= eps:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return a


def pascal(n: int) -> list[int]:
    """ Returns the n-th line of Pascals triangle.
    >>> pascal(3)
    [1, 3, 3, 1]
    """
    line = [1]
    i = 0
    while i < n:
        new_line = [1]
        j = 0
        while j < i:
            new_line.append(line[j] + line[j + 1])
            j = j + 1
        new_line.append(1)
        line = new_line
        i = i + 1
    return line