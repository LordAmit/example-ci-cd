# calculator

Sample repository for the GitHub Actions supplementary deck. The package
holds an addition and a subtraction function, and the pytest suite runs
automatically on every push.

## Try it

1. Create a new repository on GitHub.
2. Copy every file in this folder into it, including the hidden
   `.github/` folder.
3. Commit and push.
4. Open the repository's Actions tab: the `tests` workflow is running,
   and each step's log is readable while it runs.

## See a failing run

1. In `calc/arithmetic.py`, change `return a - b` to `return b - a`.
2. Commit and push.
3. The `pytest` step fails on two subtraction cases:
   `test_subtracting_three_from_five` reports that `subtract(5, 3)`
   returned -2 and the test expected 2, and the commit carries a
   failing status.
4. Revert the change and push again to return to a passing status.

## Run the suite locally

```
pip install -r requirements.txt
pytest
```
