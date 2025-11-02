# Recursion Exercises

This folder contains recursion exercises completed during my **Introduction to Programming** course in Semester 1 of my computer science degree.  
These exercises focus on applying recursive thinking to solve numerical, list-processing, and string manipulation problems without relying on Python’s built-in libraries.

## Exercises Included

### 1. Numeric Recursion
- **sum_up_to(n)** – Returns the sum of natural numbers up to n.  
- **sum_even(n)** – Returns the sum of even natural numbers up to n.  
- **sum_between(m, n)** – Returns the sum of natural numbers between m and n.  
- **factorial(n)** – Computes the factorial of n.  
- **double_factorial(n)** – Computes the factorial of odd/even numbers.  
- **logarithm(n)** – Computes the integer base-2 logarithm of n.  
- **gcd(m, n)** – Returns the greatest common divisor of m and n.  
- **lcm(m, n)** – Returns the least common multiple of m and n.  
- **first_digit(n, k=10)** – Returns the first digit of n in base k.  
- **print_multiples(k, n)** – Prints multiples of n less than k.  
- **count_divisors(n)** – Returns the number of divisors of n.  
- **is_perfect(n)** – Checks if n is a perfect number.  
- **count_perfect(n)** – Counts perfect numbers smaller than n.  
- **is_prime(n)** – Checks if n is prime.  
- **count_primes(n)** – Counts the number of primes smaller than n.  
- **sum_beyond(k)** – Returns the smallest n such that sum of numbers up to n ≥ k.  
- **is_palindrome(n)** – Checks if a number is a palindrome.  
- **find_power(k)** – Returns the smallest n such that 2^n starts with k.


### 2. Recursive List Processing
- **length(v)** – Returns the length of a list.  
- **count(x, v)** – Counts the occurrences of x in a list.  
- **member(x, v)** – Checks if x is in a list.  
- **subset(v, w)** – Checks if all elements of v occur in w.  
- **set_equals(v, w)** – Checks if two lists represent the same set.  
- **intersection(v, w)** – Returns a list of elements common to both lists.  
- **sum(v)** – Computes the sum of elements in a list.  
- **max(v)** – Returns the largest element in a list.  
- **smaller_than(n, v)** – Counts elements smaller than n.  
- **two_zeros(v)** – Checks if a list contains two consecutive zeros.  
- **even_after_7(v)** – Counts even elements after the first 7.  
- **is_sorted(v)** – Checks if a list is sorted.  
- **squares(n)** – Returns a list of squares from 1 to n.  
- **decreasing_squares(n)** – Returns a list of squares from n down to 1.  
- **divisors(n)** – Returns a list of divisors of n.  
- **square_it(v)** – Returns a list of squares of the elements in v.  
- **reverse(v)** – Returns a reversed version of the list.  
- **compare(v, n)** – Returns counts of elements larger, equal, and smaller than n.  
- **join(v, w)** – Concatenates two lists.  
- **sorted_join(v, w)** – Merges two sorted lists into one sorted list.  
- **shuffle(v, w)** – Interleaves two lists.  
- **remove(x, v)** – Returns a list excluding all occurrences of x.


### 3. Recursive String Processing
- **count(c, s)** – Counts occurrences of a character in a string.  
- **member(c, s)** – Checks if a character appears in a string.  
- **is_prefix(s1, s2)** – Checks if s1 is a prefix of s2.  
- **is_suffix(s1, s2)** – Checks if s1 is a suffix of s2.  
- **is_substring(s1, s2)** – Checks if s1 is a substring of s2.  
- **contains(s1, s2)** – Checks if s2 can be obtained from s1 by deleting characters.  
- **caesar_code(s, n)** – Applies a Caesar cipher shift to a string.  
- **to_uppercase(s)** – Converts a string to uppercase.  
- **to_lowercase(s)** – Converts a string to lowercase.  
- **toCamelCase(s)** – Converts a string to camelCase.  
- **equals_ignore_case(s1, s2)** – Checks equality ignoring case.  
- **first_position(c, s)** – Returns the index of the first occurrence of a character.  
- **last_position(c, s)** – Returns the index of the last occurrence of a character.  
- **positions(c, s)** – Returns all indices of a character in a string.  
- **is_permutation(s1, s2)** – Checks if two strings have the same characters.  
- **reverse(s)** – Reverses a string.  
- **reverse_words(s)** – Reverses each word in a string.  
- **remove_vowels(s)** – Removes all vowels from a string.  
- **encode_with_key(s, code)** – Encodes a string using a key dictionary.  
- **replicate(s, v)** – Repeats characters in a string according to a list of counts.


## Running the Code

All exercises are contained in `code/`. Each function can be imported and tested individually.  
Example:

```python
from code.recursive_programming_with_numbers import factorial
from code.recursive_programming_with_lists import length
from code.recursive_programming_with_strings import reverse

print(factorial(5))  # Output: 120
print(length([1,2,3]))  # Output: 3
print(reverse('abc'))  # Output: 'cba'
```


## Testing the Code

All functions include docstrings with usage examples. You can automatically test that the functions behave as expected using Python's built-in `doctest` module.

From the terminal, navigate to the `code/` folder and run:

```bash
python -m doctest -v recursive_programming_with_numbers.py

python -m doctest -v recursive_programming_with_lists.py

python -m doctest -v recursive_programming_with_strings.py
```