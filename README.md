# Introduction To Programming

This repository contains solutions to exercises from the Introduction to Programming course in the Python programming language.

## Getting Started

1. Clone the repository

```bash
git clone https://github.com/askmadsen/introduction-to-programming.git
cd introduction-to-programming
```

2. Install dependencies

### Requirements
- Python 3.10+
- tyro 
- pytest

Install all Python dependencies via:

```bash
pip install -r requirements.txt
```

3. Run all tests
```bash
python run.py
```

## Course Material
The repository contains exercises organized by topic and programming paradigm. Each module corresponds to one or more exercises from the course PDF:
- [Exercises PDF](exercises.pdf)

## Exercise Categories
The exercises are grouped as follows:

### Recursion
- [2 Recursive programming with numbers](recursion/numbers.py)
- [3 Recursive programming with lists](recursion/lists.py)
- [4 Recursive programming with strings](recursion/strings.py)

### Functional Programming
- [5 Functional programming](functional/functional.py)

### Imperative Programming
- [6 List comprehension](imperative/list_comprehensions.py)
- [8 Imperative programming on numbers](imperative/numbers.py)
- [9 Imperative programming on lists](imperative/lists.py)
- [10 Imperative programming on strings](imperative/strings.py)

### Small Projects
- [7 Small projects I](small_projects/small_projects_1.py)
- [11 Small projects II](small_projects/small_projects_2.py)

### Datatypes
- [Timestamp](datatypes/timestamp.py)
- [Date](datatypes/date.py)
- [Point2d](datatypes/point2d.py)
- [Polygon](datatypes/polygon.py)


## Running Tests

This project uses **[pytest](https://docs.pytest.org/)** as the testing framework together with **JSON-driven test cases**.  
Each main exercise folder (e.g. `recursion/`, `functional/`, `imperative/`, etc.) contains a `tests/` subfolder with:  

- a `test_*.py` file — the actual pytest test code  
- a `test_*_cases.json` file — the test input/output data  


### Commands And Usage

You can run tests in different scopes using the provided `run.py` helper:

| Scope | Command | Description |
|--------|----------|-------------|
| **All tests** | `python run.py` | Runs every test in the repository. |
| **A specific folder** | `python run.py --folder recursion` | Runs all tests in the *recursion* module. |
| **A specific test file** | `python run.py --folder recursion --file test_numbers.py` | Runs tests only for that file. |
| **A specific function** | `python run.py --folder recursion --file test_numbers.py --func test_sum_between` | Runs only tests for that function. |

**Note:** Any functions that are not yet implemented will be **skipped** during testing and will **not** cause an error.


### JSON Test Cases

Each test file loads its input and expected output values from a JSON file, making it easy to extend or modify tests without touching the Python code.

#### Example — recursion/tests/test_numbers_cases.json
```json
"sum_up_to": [
    [0, 0],
    [1, 1],
    [5, 15]
],

"sum_even": [
    [7, 12],
    [17, 72],
    [40, 420]
],

"sum_between": [
  [[1, 5], 15],
  [[3, 7], 25] 
]
```
Each entry is a list of test cases:

```css
[input_values, expected_output]
```
- For functions with a single argument, input_values is just the value itself.
- For functions with multiple arguments, input_values is a list containing all arguments.
- expected_output is the value that the function should return. 

#### Examples

- [5, 15] -> calls sum_up_to(5) and checks that the result equals 15.
- [[3, 7], 25] -> calls sum_between(3, 7) and checks that the result equals 25.

This structure makes it easy to add new test cases or functions without modifying the Python test code.

### Adding New Test Inputs

To add new tests, simply extend the JSON arrays with more input/output pairs.

For instance, to add another case for sum_up_to:

```json
"sum_up_to": [
    [0, 0],
    [1, 1],
    [5, 15],
    [10, 55]
]
```

Save the file and rerun your tests without the need to change the Python test file. 


### Adding A New Function To The Test Framework


1. Implement the new function in the relevant module file (e.g. recursion/numbers.py)
2. Add test cases for it to the matching JSON file. For example

```json
"new_function": [
    [0, 0],
    [1, 1],
    [5, 15],
    [10, 55]   
]
```

3. Add a corresponding test block in the test_*.py file, assuming that the desired module has been imported as module:

```python
import my_module as module  # Replace `my_module` with the actual module name

@pytest.mark.parametrize("inp,expected", cases["new_function"])
def test_new_function(inp, expected):
    if not hasattr(module, "new_function"):
        pytest.skip("new_function() not implemented yet")
    assert module.new_function(*inp) == expected
```

- Use *inp when the function takes multiple arguments (as shown above).
- For functions with a single argument, you can pass inp directly without unpacking.