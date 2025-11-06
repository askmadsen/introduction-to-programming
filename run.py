import tyro
import subprocess

def run_tests(folder: str | None = None, file: str | None = None, func: str | None = None):
    """
    Run pytest for the repo.
    
    - folder: 'recursion', 'imperative', etc.
    - file: filename, e.g., 'test_numbers.py'
    - func: function name to test, e.g., 'test_sum_between'
    """
    cmd = ["pytest"]
    if folder:
        cmd.append(f"{folder}/tests/")
    if file:
        cmd.append(f"{folder}/tests/{file}")
    if func:
        cmd.extend(["-k", func])

    subprocess.run(cmd)

if __name__ == "__main__":
    tyro.cli(run_tests)
