# Imperative programming on strings

def count(c: str, s: str) -> int:
    """ Counts the number if occurences of the character c in s.
    >>> count('a', 'banana')
    3
    """
    count = 0
    i = 0
    while i < len(s):
        if s[i] == c:
            count = count + 1
        i = i + 1
    return count


def member(c: str, s: str) -> bool:
    """ Checks wether c appears in s.
    >>> member('a', 'man')
    True
    >>> member('a', 'hut')
    False
    """
    member = False
    i = 0
    while i < len(s) and not member:
        if s[i] == c:
            member = True
        i = i + 1
    return member

def is_prefix(s1: str, s2: str) -> bool:
    """ Checks wether s1 is a prefix if s2.
    >>> is_prefix('ba', 'banana')
    True
    >>> is_prefix('bn', 'banana')
    False
    """
    if len(s1) > len(s2):
        return False
    else:
        prefix = True
        i = 0
        while i < len(s1) and prefix:
            if s1[i] != s2[i]:
                prefix = False
            i = i + 1
        return prefix 
    

def is_suffix(s1: str, s2: str) -> bool:
    """ Checks wether s1 is a suffix of s2.
    >>> is_suffix('cave', 'mancave')
    True
    >>> is_suffix('man', 'mancave')
    False
    """
    if len(s1) > len(s2):
        return False
    else: 
        i = -1
        suffix = True
        while i > -(len(s1) + 1) and suffix:
            if s1[i] != s2[i]:
                suffix = False
            i = i - 1
        return suffix
    

def contains(s1: str, s2: str) -> bool:
    """ Checks if s2 can be obtained from s1 by deleting some characters from s1.
    >>> contains('mann', 'man')
    True
    >>> contains('menn', 'man')
    False
    """
    i = 0
    j = 0
    while i < len(s2) and j < len(s1):
        if s2[i] == s1[j]:
            i = i + 1
        j = j + 1
    return i == len(s2)


def to_uppercase(s: str) -> str:
    """ Converts s to uppercase.
    >>> to_uppercase('hey')
    'HEY'  
    """
    upper = ''
    i = 0
    while i < len(s):
        if 97 <= ord(s[i]) <= 122:
            upper = upper + chr(ord(s[i]) - 32)
        else:
            upper = upper + s[i]
        i = i + 1
    return upper


def to_lowercase(s: str) -> str:
    """ Coverts s to lowercase.
    >>> to_lowercase('HEY')
    'hey'
    """
    lower = ''
    i = 0
    while i < len(s):
        if 65 <= ord(s[i]) <= 90:
            lower = lower + chr(ord(s[i]) + 32)
        else:
            lower = lower + s[i]
        i = i + 1
    return lower 


def toCamelCase(s: str) -> str:
    """ Converts s to camel notation.
    >>> toCamelCase('hey you')
    'heyYou
    """
    camel_case = ''
    i = 0
    while i < len(s):
        if s[i] == ' ':
            if 97 <= ord(s[i+1]) <= 122:
                camel_case = camel_case + chr(ord(s[i+1]) - 32)
            else:
                camel_case = camel_case + s[i + 1]
            i = i + 2
        else:
            camel_case = camel_case + s[i]
    return camel_case


def first_position(c: str, s: str) -> int:
    """ Returns the index of the first occurrence of c in s or -1 if c is not in s.
    >>> first_position('q', 'man')
    -1
    >>> first_position('a','banana')
    1
    """
    found = False
    i = 0
    while i < len(s) and not found:
        if s[i] == c:
            found = True
        i = i + 1
    if i >= len(s):
        return -1
    else:
        return i - 1
    

def last_position(c: str, s: str) -> int:
    """ Returns the index of the last occurrence of c in s or -1 if c does not appear in s.
    >>> last_position('q', 'man')
    -1
    >>> last_position('a', 'banana')
    5
    """
    found = False
    i = len(s) - 1
    while i >= 0 and not found:
        if s[i] == c:
            found = True
        i = i - 1
    if i < 0:
        return -1
    else:
        return i + 1
    

def positions(c: str, s: str) -> list[int]:
    """ Returns a list with the indices of the occurrences of c in s.
    >>> positions('a', 'banana')
    [1, 3, 5]    
    """
    positions = []
    i = 0
    while i < len(s):
        if s[i] == c:
            positions.append(i)
        i = i + 1
    return positions


def is_permutation(s1: str, s2: str) -> bool:
    """ Checks if s1 and s2 contains excatly the same characters counting repetitions.
    >>> is_permutation('abadcc', 'bcadac')
    True
    >>> is_permutation('abc', 'abcc')
    False
    """
    permutation = True
    i = 0
    if len(s1) != len(s2):
        return False
    else:
        while i < len(s1) and permutation:
            if count(s1[i], s1) != count(s1[i], s2):
                permutation = False
            i = i + 1
    return permutation


def reverse(s: str) -> str:
    """ Reverses s.
    >>> reverse('abc')
    'cba'
    """
    reverse = ''
    i = len(s) - 1
    while i >= 0:
        reverse = reverse + s[i]
        i = i - 1
    return reverse


def reverse_words(s: str) -> str:
    """ Reverses the words in s while preserving their order.
    >>> reverse_words('hey you')
    'yeh uoy'
    """
    words = []
    word = ''
    reverse_words = ''
    i = 0
    while i < len(s):
        if s[i] == ' ':
            words.append(word)
            word = ''
        else:
            word = word + s[i]
        i = i + 1
        words.append(word)
        j = 0
        while j < len(words):
            reverse_words = reverse_words + reverse(words[j]) + ' '
            j = j + 1
        return reverse_words
    

def remove_vowels(s: str) -> str:
    """ Removes the vowels in s.
    >>> remove_vowels('abce')
    'bc'
    """
    not_vowels = ''
    i = 0
    while i < len(s):
        if not member(s[i], 'aAeEiIoOuUyY'):
            not_vowels = not_vowels + s[i]
        i = i + 1
    return not_vowels


def respace(s: str, n: int) -> str:
    """ Removes all spaces from s and the adding a space after every n characters.
    >>> respace('abcdefg', 3)
    'abc def g'
    """
    words = ''
    i = 0
    while i < len(s):
        if s[i] != ' ':
            words = words + s[i]
        i = i + 1
    respace = ''
    j = 0
    while j < len(words):
        respace = respace + words[j]
        if (j + 1) % n == 0:
            respace = respace + ''
    return respace