# Small Projects

This folder contains small programming projects completed during the **Introduction to Programming** course.  
These projects explore numerical algorithms, mathematical computations, and basic numerical methods.

## Requirements
- Python 3.10+
- Standard libraries only

## Projects Included

### Prime Numbers
- **eratosthenes(n)** – Returns a list of all prime numbers ≤ `n` using the Sieve of Eratosthenes algorithm.  

```python
from code.small_projects import eratosthenes

print(eratosthenes(12))  # Output: [2, 3, 5, 7, 11]
```

### Numerical Integration
- **integral(f, a, b, n)** - Approximates the integral of a function f on [a, b] using the midpoint Riemann sum with n subdivisions.

```python 
from code.small_projects import integral

result = integral(lambda x: x**2, 0, 1, 1000)
print(result)  # Outout: 0.333
```

### Root Finding
- **bisection(f, a, b, eps)** - Approximates a solution for f(x) = 0 in [a, b] using the bisection method with precision eps.

```python
from code.small_projects import bisection

root = bisection(lambda x: x**2 - 2, 0, 2, 1e-6)
print(root)  # Output: 1.414
```

### Pascals Triangle 
- **pascal(n)** - Returns the n-th line of Pascals Triangle.

```python 
from code.small_projects import pascal

print(pascal(3))  # Output: [1, 3, 3, 1]
```


## Testing the Code

Some of the functions include docstrings with usage examples. You can test them using Python’s built-in doctest module:

From the terminal, navigate to the code/ folder and run:

```python
python -m doctest -v small_projects.py
```