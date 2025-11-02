# List Comprehensions

def squares(n: int) -> list[int]:
    """ Returns a list with the squares of numbers from 1 to n.
    >>> squares(6)
    [1, 4, 9, 16, 25, 36]
    """
    return [x * x for x in range(1, n + 1)]


def decreasing_squares(n: int) -> list[int]:
    """ Returns a list with the squares of numbers from n to 1.
    >>> decreasing_squares(6)
    [36, 25, 16, 9, 4, 1]
    """
    return [x * x for x in range(n, 0, -1)]


def count_divisors(n: int) -> int:
    """ Returns the number of divisors n has.
    >>> count_divisors(12)
    6
    """
    return len([x for x in range(1, n // 2 + 1) if n % x == 0]) + 1


def square_it(v: list[int]) -> list[int]:
    """ Returns the squares of all elements in v.
    >>> square_it([2,3,5,7,11])
    [4, 9, 25, 49, 121]
    """
    return [x * x for x in v]



def reverse(v: list) -> list:
    """ Returns v in reverse order.
    >>> reverse([1,2,3])
    [3, 2, 1]
    """
    return [v[x] for x in range(-1, -(len(v) + 1), -1)]


def remove(x: any, v: list) -> list:
    """ Removes x from v.
    >>> remove(1, [1,2,1,4,1,3,1])
    [2, 4, 3]
    """
    return [y for y in v if y != x]


def positions(c: str, s: str) -> list[int]:
    """ Returns the positions at which c occur in s.
    >>> positions('a', 'banana')
    [1, 3, 5]
    """
    return [x for x in range(len(s)) if s[x] == c]


def count(x: any, v: list) -> int:
    """ Returns the number if times x occur in v.
    >>> count(1, [0,1,1,2])
    2
    """
    return len([y for y in v if y == x])


def member(x: any, v: list) -> bool:
    """ Checks if x appear in v.
    >>> member(1, [1,2,3])
    True
    >>> member(1, [2,3])
    False
    """
    return len([y for y in v if y == x]) >= 1


def smaller_than(n: int, v: list[int]) -> int:
    """ Counts how many elements in v that are strictly smaller than n.
    >>> smaller_than(2, [1, 2, 3, 1])
    2
    """
    return len([x for x in v if x < n])


def zeros(m: int, n: int) -> list[list[int]]:
    """ Returns a zero matrix with m rows and n coloumns.
    >>> zeros(2, 3)
    [[0, 0, 0], [0, 0, 0]]
    """
    return [[0 for i in range(n)] for j in range(m)]


def identity(n: int) -> list[list[int]]:
    """ Returns a n x n matrix with 1 in the diagonal and 0 elsewhere.
    >>> identity(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    return [[1 if i == j else 0 for i in range(n)] for j in range(n)]


def triangle(n: int) -> list[list[int]]:
    """ Returns a triangular array of 1s where the first row has one elements and each
    row one more than the previous one.
    >>> triangle(4)
    [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1]]
    """
    return [[1 for i in range(j)] for j in range(1, n + 1)]


def multiplication_table(n: int) -> list[list[int]]:
    """ Returns a multiplication table up to n.
    >>> multiplication_table(4)
    [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
    """
    return [[i * j for i in range(1, n + 1)] for j in range(1, n + 1)]


def transpose(m: list[list]) -> list[int]:
    """ Returns the matrix obtained from m bi interchanging rows and coloumns.
    >>> transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """
    return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]