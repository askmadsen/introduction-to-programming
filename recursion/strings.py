from typing import List

# Recursion with strings


def count(c: str, s: str) -> int:
    """ Returnd the number of times c appears in s.
    >>> count('a', 'man')
    1
    """
    if s == '':
        return 0
    elif c == s[0]:
        return 1 + count(c, s[1:])
    else:
        return count(c, s[1:])


def member(c: str, s: str) -> bool:
    """ Checks wether c appears in s.
    >>> member('a', 'apple')
    True
    >>> member('b', 'apple')
    False
    """
    if s == '':
        return False
    elif s[0] == c:
        return True
    else:
        return member(c, s[1:])


def is_prefix(s1: str, s2: str) -> bool:
    """ Checks if s1 is a prefix of s2.
    >>> is_prefix('ap', 'apple')
    True
    >>> is_prefix('ad', 'apple')
    False
    """
    return s1 == '' or (s1[0] == s2[0] and is_prefix(s1[1:], s2[1:]))


def is_suffix(s1: str, s2: str) -> bool:
    """ Checks if s1 is a suffix of s2.
    >>> is_suffix('ple', 'apple')
    True
    >>> is_suffix('ap', 'apple')
    False
    """
    return s1 == '' or (s1[-1] == s2[-1] and is_suffix(s1[:-1], s2[:-1]))



def is_substring(s1: str, s2: str) -> bool:
    """ Checks if s1 is a substring of s2.
    >>> is_substring('al', 'apple')
    True
    >>> is_substring('ad', 'apple')
    False
    """
    return s1 == '' or (member(s1[0], s2) and is_substring(s1[1:], s2))


def contains(s1: str, s2: str) -> bool:
    """ Checks if s2 can be obtained from s1 by deleting some characters.
    >>> contains('abbce', 'abce')
    True
    >>> contains('acce', 'abce')
    False
    """
    return is_substring(s2, s1)


def caesar_code(s: str, n: int) -> str:
    """ Increases the ASCII code of each character in s by n.
    >>> caesar_code('abcd', 1)
    'bcde'
    """
    if s == '':
        return ''
    elif ord(s[0]) < 97: #checks if the character is upper case
        if ord(s[0]) + n > 90:
            return chr(ord(s[0])+ n - 26) + caesar_code(s[1:], n)
        else:
            return chr(ord(s[0]) + n) + caesar_code(s[1:], n)
    else:
        if ord(s[0]) + n > 122:
            return chr(ord(s[0])+ n - 26) + caesar_code(s[1:], n)
        else:
            return chr(ord(s[0]) + n) + caesar_code(s[1:], n)


def to_uppercase(s: str) -> str:
    """ Converts the string s to uppercase (ignoring alle non-alphabetic characters).
    >>> to_uppercase('aBcd')
    'ABCD'
    """
    if s == '':
        return ''
    elif ord(s[0]) < 97:
        return s[0] + to_uppercase(s[1:])
    else:
        return chr(ord(s[0]) - 32) + to_uppercase(s[1:])
        

def to_lowercase(s: str) -> str:
    """ Converts the string S to lowercase (ignoring all non-alphabetic characters).
    >>> to_lowercase('AcDB')
    'acdb'
    """
    if s == '':
        return ''
    elif ord(s[0]) < 97:
        return chr(ord(s[0]) + 32) + to_lowercase(s[1:])
    else:
        return s[0] + to_lowercase(s[1:])
    

def toCamelCase(s: str) -> str:
    """ Converts a string of text to camel notation.
    >>> toCamelCase('hello my friend')
    'helloMyFriend'
    """
    if s == '':
        return ''
    elif s[0] == ' ':
        return chr(ord(s[1]) - 32) + toCamelCase(s[2:])
    else:
        return s[0] + toCamelCase(s[1:])


def equals_ignore_case(s1: str, s2: str) -> bool:
    """ Determines if s1 and s2 are equal up to change of base.
    >>> equals_ignore_case('AbCd', 'aBcD')
    True
    >>> equals_ignore_case('AbCd', 'bACd')
    False
    """
    if (s1 and s2) == '':
        return True
    elif to_uppercase(s1[0]) == to_uppercase(s2[0]):
        return equals_ignore_case(s1[1:], s2[1:])
    else:
        return False


def first_position(c: str, s: str) -> int:
    """ Returns the index of the first occurrence of c in s, -1 if not found.
    >>> first_position('a', 'banana')
    1
    >>> first_position('a', 'hut')
    -1
    """
    return _first_position(c,s)

def _first_position(c: str, s: str, i: int = 0) -> int:
    if s[i:] == '':
        return -1
    elif c == s[i]:
        return i
    else:
        return _first_position(c,s, i + 1)


def last_position(c: str, s: str) -> int:
    """ Return the index of the last occurrence of c in s, -1 if not found.
    >>> last_position('a', 'banana')
    5
    >>> last_position('a', 'hut')
    -1
    """
    return _last_position(c,s)

def _last_position(c: str, s: str, i: int = -1) -> int:
    if s[:i] == '':
        return -1
    elif s[i] == c:
        return len(s) + i
    else:
        return _last_position(c,s, i - 1)


def positions(c: str, s: str) -> List[int]:
    """ Returns a list with the indices of the occurrences of c in s.
    >>> positions('a', 'banana')
    [1, 3, 5]
    >>> positions('a', 'hut')
    []
    """
    return _positions(c,s)

def _positions(c: str, s: str, i: int = 0) -> List[int]:
    if s[i:] == '':
        return []
    elif c == s[i]:
        return [i] + _positions(c, s, i + 1)
    else:
        return _positions(c, s, i + 1)
            

def is_permutation(s1: str, s2: str) -> bool:
    """ Checks if s1 and s2 contains exactly the same characters counting repetitions.
    >>> is_permutation('abbcccc', 'ccbabcc')
    True
    >>> is_permutation('aabdcc', 'baacd')
    False
    """
    return _is_permutation(s1, s2)


def _is_permutation(s1: str, s2: str, i: int = 0) -> bool:
    if s1[i:] == s2[i:] == '':
        return True
    elif count(s1[i], s1) == count(s1[i], s2):
        return _is_permutation(s1, s2, i + 1)
    else:
        return False


def reverse(s: str) -> str:
    """ Reverses the string s.
    >>> reverse('abc')
    'cba'
    """
    if s == '':
        return ''
    else:
        return s[-1] + reverse(s[:-1])
    

def reverse_words(s: str) -> str:
    """ Reverses the words in s (preserving their order).
    >>> reverse_words('hey you')
    'yeh uoy'
    """
    return _reverse_words(s)

def split(s: str, j: int = 0, i: int = 1) -> List[str]:
    if s[i:] == '':
        return [s[j:i]] # returns the last word in s
    elif s[i] == ' ':
        return [s[j:i]] + split(s, i + 1, i + 2)
    else:
        return split(s, j, i + 1)

def _reverse_words(s: str, k: int = 0) -> str:
    if split(s)[k+1:] == []:
        return reverse(split(s)[k]) 
    else:
        return reverse(split(s)[k]) + ' ' + _reverse_words(s, k + 1)
    

def remove_vowels(s: str) -> str:
    """ Removes the vowels of s.
    >>> remove_vowels('abcde')
    'bcd'
    """
    if s == '':
        return ''
    elif member(s[0], 'aAeEiIoOuUyY'):
        return remove_vowels(s[1:])
    else:
        return s[0] + remove_vowels(s[1:])


def encode_with_key(s: str, code: dict[str, str]) -> str:
    """ Encodes s with key.
    >>> encode_with_key('KYE', {'K' : 'o', 'Y' : 'l', 'E' : 't'})
    'olt'
    """
    if s == '':
        return ''
    else:
        return code[s[0]] + encode_with_key(s[1:], code)
    

def replicate(s: str, v: list[int]) -> str:
    """ Returns a string containing v[i] copies of s[i] given that len(s) == len(v).
    >>> replicate('abc', [1,2,3])
    'abbccc'
    """
    if s == '':
        return ''
    else:
        return s[0] * v[0] + replicate(s[1:], v[1:])
