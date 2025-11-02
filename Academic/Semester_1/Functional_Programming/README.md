# Functional Programming Exercises

This folder contains exercises completed during the **Introduction to Programming** course in Semester 1, focusing on **functional programming** techniques in Python.  
Key concepts practiced include using `map`, `filter`, `reduce`, and defining higher-order functions like `fixpoint` and `iterate`.

## Requirements
- Python 3.10+
- Standard libraries only

## Exercises Included

### 1. Higher-Order Functions
- **fixpoint(f, x)** – Applies `f` repeatedly until the result no longer changes.  
- **iterate(f, x, n)** – Applies `f` to `x` exactly `n` times.  

### 2. List Processing
- **sum(v)** – Returns the sum of elements using `reduce`.  
- **length(v)** – Returns the length of a list using `reduce`.  
- **remove(x, v)** – Returns a list excluding all occurrences of `x`.  
- **count_1 / count_2 / count_3(x, v)** – Counts occurrences of `x` using `map`, `filter`, or `reduce`.  
- **max(v)** – Finds the largest element using `reduce`.  
- **square_it(v)** – Returns a list of squared elements using `map`.  
- **squares(n) / decreasing_squares(n)** – Returns squares of numbers from 1 to n or n down to 1.  
- **reverse(v)** – Reverses a list using `map` and slicing.  
- **sum_up_to(n) / sum_between(m,n) / sum_even(n)** – Computes sums using `reduce`.  
- **factorial(n) / double_factorial(n)** – Computes factorials using `reduce`.  
- **member_1 / member_2(x, v)** – Checks membership using `filter` or `reduce`.  
- **subset(v, w)** – Checks if all elements of `v` are in `w`.  
- **intersection(v, w)** – Returns common elements of two lists using `filter`.  
- **smaller_than(n, v)** – Counts elements smaller than `n`.  
- **two_zeros_1 / two_zeros_2(v)** – Checks for consecutive zeros in a list.  
- **is_sorted(v)** – Checks if a list is sorted.  
- **compare(v, n)** – Returns counts of elements larger than, equal to, or smaller than `n`.  

### 3. String Processing
- **positions(c, s)** – Returns indices of occurrences of a character in a string.  
- **replicate(s, v)** – Repeats characters according to a list of counts.  
- **remove_vowels(s)** – Removes vowels from a string.  
- **caesar_code(s, n)** – Applies a Caesar cipher shift to a string.  
- **to_uppercase(s) / to_lowercase(s)** – Converts string to upper or lower case.  
- **encode_with_key(s, code)** – Encodes a string using a mapping dictionary.  


## Running the Code

All exercises are contained in `code/`. Each function can be imported and tested individually.  
Example:

```python
from code.functional_programming import factorial, sum, to_uppercase

print(factorial(5))  # Output: 120
print(sum([1,2,3]))  # Output: 6
print(to_uppercase('abc'))  # Output: 'ABC'
```


## Testing the Code

All functions include docstrings with usage examples. You can automatically test that the functions behave as expected using Python's built-in `doctest` module.

From the terminal, navigate to the `code/` folder and run:

```bash
python -m doctest -v functional_programming.py
```