# Imperative Programming Exercises

This folder contains exercises exploring **imperative programming** in Python.  
The exercises cover numbers, lists, strings, and use constructs like loops, conditionals, and list comprehensions.


## Exercises Included


### 1. List Comprehensions
- **squares(n)** – Returns the squares of numbers from 1 to n.
- **decreasing_squares(n)** – Returns squares from n down to 1.
- **count_divisors(n)** – Counts the number of divisors of n.
- **square_it(v)** – Returns the squares of all elements in a list.
- **reverse(v)** – Returns a list in reverse order.
- **remove(x, v)** – Removes all occurrences of `x` from the list.
- **positions(c, s)** – Returns indices where character `c` occurs in string `s`.
- **count(x, v)** – Counts the occurrences of `x` in a list.
- **member(x, v)** – Checks if `x` appears in a list.
- **smaller_than(n, v)** – Counts elements in a list smaller than `n`.
- **zeros(m, n)** – Returns an m×n zero matrix.
- **identity(n)** – Returns an n×n identity matrix.
- **triangle(n)** – Returns a triangular array of 1s.
- **multiplication_table(n)** – Returns a multiplication table up to n.
- **transpose(m)** – Transposes a matrix.



### 2. Numeric Computation

- **print_multiples(k, n)** – Prints the multiples of `k` less than or equal to `n`.  
- **sum_up_to(n)** – Returns the sum of natural numbers from 1 to `n`.  
- **sum_even(n)** – Returns the sum of even numbers from 1 to `n`.  
- **sum_between(m, n)** – Returns the sum of numbers between `m` and `n`.  
- **sum_beyond(k)** – Returns the smallest `n` such that `sum_up_to(n)` ≥ `k`.  
- **factorial(n)** – Returns the factorial of `n`.  
- **double_factorial(n)** – Returns the double factorial of `n`.  
- **fibonacci(n)** – Returns the `n`th Fibonacci number.  
- **logarithm(n, m=2)** – Returns the integer base-`m` logarithm of `n`.  
- **count_divisors(n)** – Returns the number of divisors of `n`.  
- **is_perfect(n)** – Checks if `n` is a perfect number.  
- **count_perfect(n)** – Counts the perfect numbers smaller than `n`.  
- **is_prime(n)** – Checks if `n` is prime.  
- **count_primes(n)** – Counts the prime numbers smaller than `n`.  
- **nth_prime(n)** – Returns the `n`th prime number.  
- **gcd(m, n)** – Returns the greatest common divisor of `m` and `n`.  


### 3. List Processing
- **sum(v)** – Returns the sum of all elements in `v`.  
- **count(x, v)** – Counts the occurrences of `x` in `v`.  
- **max(v)** – Returns the maximum element in `v`.  
- **smaller_than(n, v)** – Counts elements in `v` strictly smaller than `n`.  
- **squares(n)** – Returns a list of squares from 1 to `n`.  
- **decreasing_squares(n)** – Returns a list of squares from `n` down to 1.  
- **divisors(n)** – Returns a list of divisors of `n`.  
- **two_zeros(v)** – Checks whether `v` contains two consecutive zeros.  
- **is_sorted(v)** – Checks whether `v` is sorted.  
- **member(x, v)** – Checks whether `x` appears in `v`.  
- **subset(v, w)** – Checks if `v` is a subset of `w`.  
- **intersection(v, w)** – Returns elements that appear in both `v` and `w`.  
- **first_position_max(s)** – Index of first occurrence of the max element.  
- **last_position_max(s)** – Index of last occurrence of the max element.  
- **add_positions_max(s)** – Sum of indices of max elements.  
- **positions_max(s)** – List of indices of max elements.  
- **square_it(v)** – Replaces elements of `v` with their squares (in place).  
- **reverse(v)** – Returns a reversed copy of `v`.  
- **even_after_first_7(v)** – Counts even numbers after the first 7.  
- **even_after_last_7(v)** – Counts even numbers after the last 7.  
- **sorted_join(v, w)** – Merges two sorted lists into one sorted list.  
- **shuffle(v, w)** – Returns a list with alternating elements from `v` and `w`.  
- **largest_increasing_sequence(v)** – Length of the longest increasing consecutive sequence.  
- **dimensions(m)** – List of row lengths for a 2D list.  
- **is_matrix(m)** – Checks if all rows of `m` have the same length.  
- **is_square_matrix(m)** – Checks if `m` is a square matrix.  
- **zeros(m, n)** – Creates an `m x n` zero matrix.  
- **identity(n)** – Creates an `n x n` identity matrix.  
- **triangle(n)** – Creates a triangular array of 1s.  
- **multiplication_table(n)** – Creates an `n x n` multiplication table.  
- **sum_all(m)** – Sum of all values in a 2D list.  
- **max_all(m)** – Maximum element in a 2D list.  
- **parity(m)** – Converts even numbers to 0 and odd numbers to 1 (in place).  
- **trace(m)** – Sum of the main diagonal in a square matrix.  
- **column(m, j)** – Returns the `j`th column of a matrix.  
- **add(m1, m2)** – Element-wise sum of two matrices.  
- **multiply(a, m)** – Multiplies all entries in a matrix by `a` (in place).  
- **del_row_and_col(m, i, j)** – Returns `m` without the `i`th row and `j`th column.  
- **differences(v)** – Returns an array of differences between consecutive elements repeatedly.  
- **transpose(m)** – Returns `m` with rows and columns interchanged.  
- **product(m1, m2)** – Matrix multiplication of `m1` and `m2`.  


### 4. String Processing
- **count(c, s)** – Counts occurrences of character `c` in `s`.  
- **member(c, s)** – Checks if `c` appears in `s`.  
- **is_prefix(s1, s2)** – Checks if `s1` is a prefix of `s2`.  
- **is_suffix(s1, s2)** – Checks if `s1` is a suffix of `s2`.  
- **contains(s1, s2)** – Checks if `s2` can be obtained from `s1` by deleting some characters.  
- **to_uppercase(s)** – Converts `s` to uppercase.  
- **to_lowercase(s)** – Converts `s` to lowercase.  
- **toCamelCase(s)** – Converts `s` to camelCase.  
- **first_position(c, s)** – Index of first occurrence of `c` in `s`, or -1 if not found.  
- **last_position(c, s)** – Index of last occurrence of `c` in `s`, or -1 if not found.  
- **positions(c, s)** – List of indices of occurrences of `c` in `s`.  
- **is_permutation(s1, s2)** – Checks if `s1` and `s2` contain the same characters with the same counts.  
- **reverse(s)** – Returns the reversed string.  
- **reverse_words(s)** – Reverses each word in `s` while preserving word order.  
- **remove_vowels(s)** – Removes all vowels from `s`.  
- **respace(s, n)** – Removes all spaces from `s` and inserts a space every `n` characters.


## Running the Code

All exercises are contained in `code/`. Each function can be imported and tested individually.  
Example:

```python
from code.list_comprehensions import squares, remove, multiplication_table

print(squares(6))  
# Output: [1, 4, 9, 16, 25, 36]

print(remove(1, [1,2,1,4,1,3,1]))  
# Output: [2, 4, 3]

print(multiplication_table(4))  
# Output: [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
```

```python
from code.imperative_programming_on_numbers import sum_up_to, factorial, is_prime, nth_prime, gcd

print(sum_up_to(10))       # Output: 55
print(factorial(5))        # Output: 120
print(is_prime(7))         # Output: True
print(nth_prime(5))        # Output: 11
print(gcd(24, 36))         # Output: 12
```

```python
from code.imperative_programming_on_lists import sum, reverse, sorted_join, multiply

v = [1, 2, 3, 4]
print(sum(v))                       # Output: 10
print(reverse(v))                   # Output: [4, 3, 2, 1]
print(sorted_join([1,3],[2,4]))     # Output: [1, 2, 3, 4]
m = [[1,2],[3,4]]
multiply(2, m)
print(m)                            # Output: [[2, 4], [6, 8]]
```


```python
from code.imperative_programming_on_strings import count, member, is_prefix, to_uppercase, remove_vowels

s = 'banana'
print(count('a', s))                # Output: 3
print(member('x', s))               # Output: False
print(is_prefix('ba', s))           # Output: True
print(to_uppercase('hello'))        # Output: 'HELLO'
print(remove_vowels('alphabet'))    # Output: 'lphbt'
```

## Testing the Code

All functions include docstrings with usage examples. You can automatically test that the functions behave as expected using Python's built-in `doctest` module.

From the terminal, navigate to the `code/` folder and run:

```bash
python -m doctest -v list_comprehensions.py

python -m doctest -v imperative_programming_on_numbers.py

python -m doctest -v imperative_programming_on_lists.py

python -m doctest -v imperative_programming_on_strings.py
```