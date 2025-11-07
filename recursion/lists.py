# 3 Recursive programming with lists
    
def length(v: list) -> int:
    """Returns the length of the list v."""
    if v == []:
        return 0 
    else:
        return 1 + length(v[1:])

def count(x: any, v: list) -> int:
    """Returns the number of times x occurs in v."""
    if v == []:
        return 0
    elif x == v[0]:
        return 1 + count(x, v[1:])
    else:
        return count(x, v[1:])
    
def member(x: any, v: list) -> bool:
    """Checks if x is in the list v."""
    if v == []:
        return False
    elif x == v[0]:
        return True
    else:
        return member(x, v[1:])

def subset(v: list, w: list) -> bool:
    """Checks if all elements of v occur in w."""
    return (v == [] or (member(v[0], w) and subset(v[1:], w)))
    
def set_equals(v: list, w: list) -> bool:
    """Checks if v and w represent the same set."""
    return subset(v,w) and subset(w,v)

def intersection(v: list, w: list) -> list:
    """ Returns a list containing the element that occur both in v and w."""
    if v == []:
        return []
    elif member(v[0], w):
        return [v[0]] + intersection(v[1:], w)
    else:
        return intersection(v[1:], w)

def sum(v: list[int]) -> int:
    """ Returns the sum of the elements in v."""
    if v == []:
        return 0
    else:
        return v[0] + sum(v[1:])

def max(v: list[int]) -> int:
    """ Returns the largest element in v =! []."""
    return _max(v)

def _max(v: list[int], i: int = 1, j: int = 0) -> int:
    if v[i:] == []:
        return v[j]
    elif v[j] >= v[i]:
        return _max(v,i + 1, j)
    else:
        return _max(v, i + 1, i)

def smaller_than(n: int, v: list[int]) -> int:
    """ Returns the number of elements in v strictly smaller than n."""
    if v == []:
        return 0
    elif v[0] < n:
        return 1 + smaller_than(n, v[1:])
    else:
        return smaller_than(n, v[1:])

def two_zeros(v: list[int]) -> bool:
    """ Checks if v contains 2 consecutive zeros."""
    return _two_zeros(v)

def _two_zeros(v: list[int], i: int = 0) -> bool:
    if v[i + 1:] == []:
        return False
    elif v[i] == v[i + 1] == 0:
        return True
    else:
        return _two_zeros(v, i + 1)

def even_after_7(v: list[int]) -> int:
    """ Computes the number of even elements in v occuring after the first 7."""
    if v == []:
        return 0
    elif v[0] == 7:
        return _even_after_7(v[1:])
    else:
        return even_after_7(v[1:])

def _even_after_7(v: list[int]) -> int:
    if v == []:
        return 0
    elif v[0] % 2 == 0:
        return 1 + _even_after_7(v[1:])
    else:
        return _even_after_7(v[1:])

def is_sorted(v: list[int]) -> bool:
    """ Checks if v is sorted."""
    return len(v) <= 1 or (v[0] <= v[1] and is_sorted(v[1:]))

def squares(n: int) -> list[int]:
    """ Returns a list with the squares of numbers from 1 to n."""
    if n == 0:
        return []
    else:
        return squares(n-1) + [n * n]

def decreasing_squares(n: int) -> list[int]:
    """ Returns a list with squares of the numbers n to 1."""
    if n > 0:
        return [n ** 2] + decreasing_squares(n - 1)
    else:
        return []

def divisors(n: int) -> list[int]:
    """ Returns a list containing the divisors of n."""
    return _divisors(n)

def _divisors(n: int, i: int = 1) -> list[int]:
    if n == i:
        return [i]
    elif n % i == 0:
        return [i] + _divisors(n, i + 1)
    else:
        return _divisors(n, i + 1)

def square_it(v: list[int]) -> list[int]:
    """ Return a list containing the squares of v."""
    return _square_it(v)

def _square_it(v: list[int], i: int = 0) -> list[int]:
    if v[i:] == []:
        return []
    else:
        return [v[i] ** 2] + _square_it(v, i + 1)

def reverse(v: list[int]) -> list[int]:
    """ Returns a list with the elements in v in reversed order."""
    if v == []:
        return []
    else:
        return [v[-1]] + reverse(v[:-1])

def compare(v: list[int], n: int) -> tuple[int, int, int]:
    """ Returns a tuple containing number of elements in v larger, equal to and smaller than n."""
    if v == []:
        return (0, 0, 0)
    else:
        (gt, eq, lt) = compare(v[1:], n)
        if v[0] > n:
            return (gt + 1, eq, lt)
        elif v[0] == n:
            return (gt, eq + 1, lt)
        else:
            return (gt, eq, lt + 1)

def join(v: list, w: list) -> list:
    """ Returns a list with the elements of v followed by the elements of w."""
    return v + w

def sorted_join(v: list[int], w: list[int]) -> list[int]:
    """ Returns one sorted list from two sorted lists v and w."""
    if v == []:
        return w
    elif v[0] <= w[0]:
        return [v[0]] + sorted_join(v[1:], w)
    else:
        return [w[0]] + sorted_join(w[1:], v)
    
def shuffle(v: list, w: list) -> list:
    """ Shuffles v and w."""
    if v == []:
        return w
    else:
        return [v[0]] + shuffle(w, v[1:])

def remove(x: any, v: list) -> list:
    """ Returns a list containing all elements in v different from x."""
    if v == []:
        return []
    elif x == v[0]:
        return remove(x, v[1:])
    else:
        return [v[0]] + remove(x, v[1:])