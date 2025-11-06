# Imperative programming on lists


def sum(v: list[int]) -> int:
    """ Returns the sum of all elements in v.
    >>> sum([1,2,3])
    6
    """
    sum = 0
    i = 0
    while i < len(v):
        sum = sum + v[i]
        i = i + 1
    return sum


def count(x: any, v: list) -> int:
    """ Returns the number of times x appear in v.
    >>> count(1, [2,1,3,1])
    2
    """
    count = 0
    i = 0
    while i < len(v):
        if v[i] == x:
            count = count + 1
        i = i + 1
    return count


def max(v: list[int]) -> int:
    """ Returns the max element in v.
    >>> max([1,3,7,7,6,8,2])
    8
    """
    max = v[0]
    i = 0
    while i < len(v):
        if v[i] > max:
            max = v[i]
        i = i + 1
    return max


def smaller_than(n: int, v: list[int]) -> int:
    """ Counts the number of elements in v that are strictly smaller than n.
    >>> smaller_than(4, [4, 5, 6, 2, 1])
    2
    """
    count = 0
    i = 0
    while i < len(v):
        if v[i] < n:
            count = count + 1
        i = i + 1
    return count


def squares(n: int) -> list[int]:
    """ Returns a list with the squares of numbers from 1 to n.
    >>> squares(5)
    [1, 4, 9, 16, 25]
    """
    squares = []
    i = 1
    while i <= n:
        squares.append(i * i)
        i = i + 1
    return squares


def decreasing_squares(n: int) -> list[int]:
    """ Returns a list with the squares of numbers from n to 1.
    >>> decreasing_squares(5)
    [25, 16, 9, 4, 1]
    """
    squares = []
    i = n
    while i >= 1:
        squares.append(i * i)
        i = i - 1
    return squares


def divisors(n: int) -> list[int]:
    """ Returns a list containing the divisors of n.
    >>> divisors(12)
    [1, 2, 3, 4, 6, 12]
    """
    divisors = []
    i = 1
    while i <= n:
        if n % i == 0:
            divisors.append(i)
        i = i + 1
    return divisors


def two_zeros(v: list[int]) -> bool:
    """ Checks wether v contains two consecutive zeros.
    >>> two_zeros([1,0,0,2])
    True
    >>> two_zeros([0,1,0,1,0])
    False
    """
    found = False
    i = 0
    while not found and i < len(v) - 1:
        if v[i] == v[i + 1] == 0:
            found = True
        i = i + 1
    return found


def is_sorted(v: list[int]) -> bool:
    """Checks wether v is sorted
    >>> is_sorted([0,1,2,2,4,7])
    True
    >>> is_sorted([0,1,0,3,4])
    False
    """
    sorted = True
    i = 0
    while sorted and i < len(v) - 1:
        if v[i] > v[i + 1]:
            sorted = False
        i = i + 1
    return sorted


def member(x: any, v: list) -> bool:
    """ Checks wether x appears in v.
    >>> member(1, [0,1,2])
    True
    >>> member(1, [0,2,3])
    False
    """
    found = False
    i = 0
    while not found and i < len(v):
        if v[i] == x:
            found = True
        i = i + 1
    return found


def subset(v: list, w: list) -> bool:
    """ Checks wether v is a subset of w.
    >>> subset([1,2,2,3], [1,2,3,4])
    True
    >>> subset([1,2,3],[1,1,3])
    False
    """
    subset = True
    i = 0
    while subset and i < len(v):
        if not member(v[i] ,w):
            subset = False
        i = i + 1
    return subset


def intersection(v: list, w: list) -> list:
    """ Returns a list with elements that both occur in v and w.
    >>> intersection([1,3,5,6,9],[1,2,5,7,9])
    [1, 5, 9]
    """
    intersect = []
    i = 0
    while i < len(v):
        if member(v[i], w):
            intersect.append(v[i])
        i = i + 1
    return intersect


def first_position_max(s: list[int]) -> int:
    """ Returns the index of the first occurrence of the max element in s or -1 if s is empty
    >>> first_position_max([1,7,3,5,7])
    1
    >>> first_position_max([])
    -1
    """
    if s == []:
        return -1
    else:
        i = 0
        max = s[0]
        pos = 0
        while i < len(s):
            if s[i] > max:
                max = s[i]
                pos = i
            i = i + 1
        return pos


def last_position_max(s: list[int]) -> int:
    """ Returnd the index of the last occurrence of the max element in s or -1 if s is empty.
    >>> last_position_max([1,7,3,5,7,3])
    4
    >>> last_position_max([])
    -1
    """
    if s == []:
        return -1
    else:
        i = 0
        max = s[0]
        pos = 0
        while i < len(s):
            if s[i] >= max:
                max = s[i]
                pos = i
            i = i + 1
        return pos


def add_positions_max(s: list[int]) -> int:
    """ Returns the sum of the indices of max elements in s.
    >>> add_positions_max([1,7,3,5,7])
    5
    >>> add_positions_max([])
    -1
    """
    if s == []:
        return -1
    else:
        sum = 0
        max = s[0]
        i = 0
        while i < len(s):
            if s[i] == max:
                sum = sum + i
            elif s[i] > max:
                max = s[i]
                sum = i
            i = i + 1
        return sum


def positions_max(s: list[int]) -> list[int]:
    """ Returns a list with the indices of the positions of the max elements in s.
    >>> positions_max([1,7,3,5,7])
    [1, 4]
    """
    positions = []
    i = 0
    if s != []:
        max = s[0]
    while i < len(s):
        if s[i] > max:
            positions = [i]
            max = s[i]
        elif s[i] == max:
            positions.append(i)
        i = i + 1
    return positions


def square_it(v: list[int]) -> None:
    """ Replaces each element in v with its square.
    """
    i = 0
    while i < len(v):
        v[i] = v[i] ** 2
        i = i + 1


def reverse(v: list) -> list:
    """ Reverses v.
    >>> reverse([0,1,2,3])
    [3, 2, 1, 0]
    """
    reverse = []
    i = len(v) - 1
    while i >= 0:
        reverse.append(v[i])
        i = i - 1
    return reverse


def even_after_first_7(v: list[int]) -> int:
    """ Returns the number of even elements after the first 7.
    >>> even_after_first_7([0,7,3,2,4,5])
    2
    """
    i = 0
    while i < len(v) and v[i] != 7:
        i = i + 1
    count = 0
    while i < len(v):
        if v[i] % 2 == 0:
            count = count + 1
        i = i + 1
    return count


def even_after_last_7(v: list[int]) -> int:
    """ Returns the number of even elements after the last 7.
    >>> even_after_last_7([0,7,3,1,7,2,3,4])
    2
    """
    i = len(v) - 1
    count = 0
    while i >= 0 and v[i] != 7:
        if v[i] % 2 == 0:
            count = count + 1
        i = i - 1
    if i < 0:
        return 0
    else:
        return count


def sorted_join(v: list[int], w: list[int]) -> list[int]:
    """ Takes two sorted lists and returns a sorted joint list.
    >>> sorted_join([0,1,3,5,6],[1,2,4,6])
    [0, 1, 1, 2, 3, 4, 5, 6, 6]
    """
    joint = []
    i = 0
    j = 0
    while i < len(v) and j < len(w):
        if v[i] <= w[j]:
            joint.append(v[i])
            i = i + 1
        else:
            joint.append(w[j])
            j = j + 1
    if i >= len(v):
        joint = joint + w[j:]
    else:
        joint = joint + v[i:]
    return joint


def shuffle(v: list, w: list) -> list:
    """ Returns a list containing alternating elements of v and w.
    >>> shuffle([1,2,3,4],[5,6,7])
    [1, 5, 2, 6, 3, 7, 4]
    """
    shuffle = []
    i = 0
    while i < len(v) and i < len(w):
        shuffle.extend([v[i], w[i]]) # appends more than 1 element
        i = i + 1
    if i >= len(v):
        shuffle = shuffle + w[i:]
    else:
        shuffle = shuffle + v[i:]
    return shuffle


def largest_increasing_sequence(v: list) -> int:
    """ Returns the length of the largest increasing sequence of consecutive elements.
    >>> largest_increasing_sequence([1,2,4,3,5,7,2,3,4,5,2,3])
    4
    """
    count = 0
    counts = 0
    max = v[0]
    i = 1
    while i < len(v):
        if v[i] >= max:
            count = count + 1
            max = v[i]
        elif v[i] < max:
            if count > counts:
                counts = count
            count = 1
            max = v[i]
        i = i + 1
    if counts > count:
        return counts
    else:
        return count


def dimensions(m: list[list]) -> list[int]:
    """ Returns a list witht he lengths of all elements in m.
    >>> dimensions([[1,2],[1,2,3],[1]])
    [2, 3, 1]
    """
    dim = []
    i = 0
    while i < len(m):
        dim.append(len(m[i]))
        i = i + 1
    return dim


def is_matrix(m: list[list]) -> bool:
    """ Checks wether m is a matrix.
    >>> is_matrix([[1,2],[2,3],[3,4]])
    True
    >>> is_matrix([[1,2],[1,2,3]])
    False
    """
    size = len(m[0])
    i = 1
    while i < len(m) and size == len(m[i]):
        i = i + 1
    return i >= len(m)
        

def is_square_matrix(m: list[list]) -> bool:
    """ Checks if m is a square matrix.
    >>> is_square_matrix([[2,3],[3,4]])
    True
    >>> is_square_matrix([[2,3],[3,4],[4,5]])
    False
    """
    i = 0
    while i < len(m) and len(m) == len(m[i]):
        i = i + 1
    return i >= len(m)
    

def zeros(m: int, n: int) -> list[list[int]]:
    """ Returns a zero matrix with m rows and n columns.
    >>> zeros(3,2)
    [[0, 0], [0, 0], [0, 0]]
    """
    mat = []
    i = 0
    while i < m:
        row = []
        j = 0
        while j < n:
            row.append(0)
            j = j + 1
        mat.append(row)
        i = i + 1
    return mat


def identity(n: int) -> list[list[int]]:
    """ Returns a matrix of size n x n with 1's on the diagonal and 0 elsewhere.
    >>> identity(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    identity = []
    i = 0
    while i < n:
        row = []
        j = 0
        while j < n:
            if i == j:
                row.append(1)
            else:
                row.append(0)
            j = j + 1
        identity.append(row)
        i = i + 1
    return identity


def triangle(n: int) -> list[list[int]]:
    """ Returns a triangular array of 1's with the first row containing 1 element and each row afterwards
        containing 1 more element than the previous
    >>> triangle(3)
    [[1], [1, 1], [1, 1, 1]]
    """
    triangle = []
    i = 0
    while i < n:
        row = []
        j = 0
        while j < i + 1:
            row.append(1)
            j = j + 1
        triangle.append(row)
        i = i + 1
    return triangle


def multiplication_table(n: int) -> list[list[int]]:
    """ Returns a multiplication table up to n.
    >>> multiplication_table(4)
    [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
    """
    mult_table = []
    i = 1
    while i <= n:
        row = []
        j = 1
        while j <= n:
            row.append(i * j)
            j = j + 1
        mult_table.append(row)
        i = i + 1
    return mult_table


def sum_all(m: list[list[int]]) -> int:
    """ Returns the summ of all values in the list of lists m.
    >>> sum_all([[1,2,3], [2,3,4], [-1,-3,-5]])
    6
    """
    sum = 0
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            sum = sum + m[i][j]
            j = j + 1
        i = i + 1
    return sum


def max_all(m: list[list[int]]) -> int:
    """ Returns the largest element in the nonempty list of lists m.
    >>> max_all([[1,-2,3],[4,-7,6]])
    6
    """
    max = m[0][0]
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            if m[i][j] > max:
                max = m[i][j]
            j = j + 1
        i = i + 1
    return max


def parity(m: list[list[int]]) -> None:
    """ Replaces even elements in m with 0 and odd elements with 1.
    """
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            if m[i][j] % 2 == 0:
                m[i][j] = 0
            else:
                m[i][j] = 1
            j = j + 1
        i = i + 1


def trace(m: list[list[int]]) -> int:
    """ Returns the sum of the diagonal if m is a square matrix.
    >>> trace([[1,2,3],[4,5,6],[7,8,9]])
    15
    """
    trace = 0
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            if j == i:
                trace = trace + m[i][j]
            j = j + 1
        i = i + 1
    return trace


def column(m: list[list], j: int) -> list:
    """ Returns the j-th column of the matrix m.
    >>> column([[1,2,3],[4,5,6],[7,8,9]], 2)
    [2, 5, 8]
    """
    column = []
    i = 0
    while i < len(m):
        column.append(m[i][j-1])
        i = i + 1
    return column


def add(m1: list[list[int]], m2: list[list[int]]) -> list[list]:
    """ Adds the two matrices entry by entry
    >>> add([[1,2],[3,4]], [[-1,-2],[-3,-4]])
    [[0, 0], [0, 0]]
    """
    m = []
    i = 0
    while i < len(m1):
        row = []
        j = 0
        while j < len(m1[i]):
            row.append(m1[i][j] + m2[i][j])
            j = j + 1
        m.append(row)
        i = i + 1
    return m


def multiply(a: int, m: list[list[int]]) -> None:
    """ Multiplies all entries in m by a.
    """
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            m[i][j] = m[i][j] * a
            j = j + 1
        i = i + 1


def del_row_and_col(m: list[list[int]], i: int, j: int) -> list[list[int]]:
    """ Returns the matrix obtained by removing the i-th row and j-th column.
    >>> del_row_and_col([[1,2,3],[4,5,6],[7,8,9]], 2, 2)
    [[1, 3], [7, 9]]
    """
    mat = []
    ii = 0
    while ii < len(m):
        row = []
        jj = 0
        while jj< len(m[ii]):
            if jj != j - 1 and ii != i - 1:
                row.append(m[ii][jj])
            jj = jj + 1
        if row != []:
            mat.append(row)
        ii = ii + 1
    return mat


def differences(v: list[int]) -> list[list[int]]:
    """ Returns an array of arrays such that the first line is v and each consecutive
        line contains the differences between each element in the previous line.
    >>> differences([2, 1, 5 ,-2])
    [[2, 1, 5, -2], [1, -4, 7], [5, -11], [16]]
    """
    diff = [v]                               
    n = len(v)                        
    i = 1
    while i < n:
        row = []
        j = 0
        while j < len(v) - 1:
            row.append(v[j] - v[j + 1])
            j = j + 1
        diff.append(row)
        v = row
        i = i + 1
    return diff


def transpose(m: list[list]) -> list[list]:
    """ Returns m with its rows and columns interchenged.
    >>> transpose([[1,2,3],[4,5,6],[7,8,9]])
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """
    transpose = []
    i = 0
    while i < len(m[0]):
        row = []
        j = 0
        while j < len(m):
            row.append(m[j][i])
            j = j + 1
        transpose.append(row)
        i = i + 1
    return transpose


def product(m1: list[list[int]], m2: list[list[int]]) -> list[list[int]]:
    """ Returns the matrix multiplication of m1 and m2.
    >>> product([[1,2,3],[4,5,6],[7,8,9]], [[2,4,6],[1,2,3],[5,2,1]])
    [[19, 14, 15], [43, 38, 45], [67, 62, 75]]
    """
    m = []
    i = 0
    while i < len(m1):
        row = []
        j = 0
        while j < len(m2[0]):
            entry = 0
            k = 0
            while k < len(m2): # or k < len(m1[0])
                entry = entry + m1[i][k] * m2[k][j]
                k = k + 1
            row.append(entry)
            j = j + 1
        m.append(row)
        i = i + 1
    return m