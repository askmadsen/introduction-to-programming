from typing import List

# Recursive programming with lists
    
def length(v: list) -> int:
    """Returns the length of the list v.
    >>> length([1,2,3,4,5])
    5
    """
    if v == []:
        return 0 
    else:
        return 1 + length(v[1:])


def count(x: any, v: list) -> int:
    """Returns the number of times x occurs in v.
    >>> count(2, [2,4,5,3,2])
    2
    """
    if v == []:
        return 0
    elif x == v[0]:
        return 1 + count(x, v[1:])
    else:
        return count(x, v[1:])
    

def member(x: any, v: list) -> bool:
    """Checks if x is in the list v.
    >>> member(2, [0,1,3,4])
    False
    >>> member(2, [1,2])
    True
    """
    if v == []:
        return False
    elif x == v[0]:
        return True
    else:
        return member(x, v[1:])


def subset(v: list, w: list) -> bool:
    """Checks if all elements of v occur in w.
    >>> subset([0,1], [0,1,2])
    True
    >>> subset([0,2], [0,1,3])
    False
    """
    return (v == [] or (member(v[0], w) and subset(v[1:], w)))
    


def set_equals(v: list, w: list) -> bool:
    """Checks if v and w represent the same set.
    >>> set_equals([3,1,2], [1,2,3])
    True
    """
    return subset(v,w) and subset(w,v)


def intersection(v: list, w: list) -> list:
    """ Returns a list containing the element that occur both in v and w.
    >>> intersection([0,2,4],[0,1,4,5])
    [0, 4]
    """
    if v == []:
        return []
    elif member(v[0], w):
        return [v[0]] + intersection(v[1:], w)
    else:
        return intersection(v[1:], w)


def sum(v: List[int]) -> int:
    """ Returns the sum of the elements in v.
    >>> sum([1,2,3])
    6
    """
    if v == []:
        return 0
    else:
        return v[0] + sum(v[1:])



def max(v: List[int]) -> int:
    """ Returns the largest element in v =! [].
    >>> max([1,3,2])
    3
    """
    return _max(v)

def _max(v: List[int], i: int = 1, j: int = 0) -> int:
    if v[i:] == []:
        return v[j]
    elif v[j] >= v[i]:
        return _max(v,i + 1, j)
    else:
        return _max(v, i + 1, i)


def smaller_than(n: int, v: List[int]) -> int:
    """ Returns the number of elements in v strictly smaller than n.
    >>> smaller_than(3, [0,2,3])
    2
    """
    if v == []:
        return 0
    elif v[0] < n:
        return 1 + smaller_than(n, v[1:])
    else:
        return smaller_than(n, v[1:])


def two_zeros(v: List[int]) -> bool:
    """ Checks if v contains 2 consecutive zeros.
    >>> two_zeros([0,1,0])
    False
    >>> two_zeros([1,0,0])
    True
    """
    return _two_zeros(v)

def _two_zeros(v: List[int], i: int = 0) -> bool:
    if v[i + 1:] == []:
        return False
    elif v[i] == v[i + 1] == 0:
        return True
    else:
        return _two_zeros(v, i + 1)


def even_after_7(v: List[int]) -> int:
    """ Computes the number of even elements in v occuring after the first 7.
    >>> even_after_7([1,2,3,7,4,2,3])
    2
    """
    if v == []:
        return 0
    elif v[0] == 7:
        return _even_after_7(v[1:])
    else:
        return even_after_7(v[1:])

def _even_after_7(v: List[int]) -> int:
    if v == []:
        return 0
    elif v[0] % 2 == 0:
        return 1 + _even_after_7(v[1:])
    else:
        return _even_after_7(v[1:])
  

def is_sorted(v: List[int]) -> bool:
    """ Checks if v is sorted.
    >>> is_sorted([1,2,3])
    True
    >>> is_sorted([3,2,1])
    False
    """
    return len(v) <= 1 or (v[0] <= v[1] and is_sorted(v[1:]))



def squares(n: int) -> List[int]:
    """ Returns a list with the squares of numbers from 1 to n.
    >>> squares(4)
    [1, 4, 9, 16]
    """
    if n == 0:
        return []
    else:
        return squares(n-1) + [n * n]


def decreasing_squares(n: int) -> List[int]:
    """ Returns a list with squares of the numbers n to 1.
    >>> decreasing_squares(3)
    [9, 4, 1]
    """
    if n > 0:
        return [n ** 2] + decreasing_squares(n - 1)
    else:
        return []


def divisors(n: int) -> List[int]:
    """ Returns a list containing the divisors of n.
    >>> divisors(4)
    [1, 2, 4]
    """
    return _divisors(n)

def _divisors(n: int, i: int = 1) -> List[int]:
    if n == i:
        return [i]
    elif n % i == 0:
        return [i] + _divisors(n, i + 1)
    else:
        return _divisors(n, i + 1)


def square_it(v: List[int]) -> List[int]:
    """ Return a list containing the squares of v.
    >>> square_it([2,3])
    [4, 9]
    """
    return _square_it(v)

def _square_it(v: List[int], i: int = 0) -> List[int]:
    if v[i:] == []:
        return []
    else:
        return [v[i] ** 2] + _square_it(v, i + 1)


def reverse(v: list[int]) -> list[int]:
    """ Returns a list with the elements in v in reversed order.
    >>> reverse([1,2,3])
    [3, 2, 1]
    """
    if v == []:
        return []
    else:
        return [v[-1]] + reverse(v[:-1])
    return _reverse(v)


def compare(v: list[int], n: int) -> (int, int, int):
    """ Returns a tuple containing number of elements in v larger, equal to and smaller than n.
    >>> compare([1,2,3,4], 2)
    (2, 1, 1)
    """
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
    """ Returns a list with the elements of v followed by the elements of w.
    >>> join([0,1,2], [3,5,4])
    [0, 1, 2, 3, 5, 4]
    """
    return v + w

def sorted_join(v: list[int], w: list[int]) -> list[int]:
    """ Returns one sorted list from two sorted lists v and w.
    >>> sorted_join([1,4,6],[2,4,5])
    [1, 2, 4, 4, 5, 6]
    """
    if v == []:
        return w
    elif v[0] <= w[0]:
        return [v[0]] + sorted_join(v[1:], w)
    else:
        return [w[0]] + sorted_join(w[1:], v)
    
    
def shuffle(v: list, w: list) -> list:
    """ Shuffles v and w.
    >>> shuffle([2,4], [1,2,3])
    [2, 1, 4, 2, 3]
    """
    if v == []:
        return w
    else:
        return [v[0]] + shuffle(w, v[1:])


def remove(x: any, v: list) -> list:
    """ Returns a list containing all elements in v different from x.
    >>> remove(2, [1,2,3,2])
    [1, 3]
    """
    if v == []:
        return []
    elif x == v[0]:
        return remove(x, v[1:])
    else:
        return [v[0]] + remove(x, v[1:])