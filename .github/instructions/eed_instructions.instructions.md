---
applyTo: '**/*.py'
---
Coding standards, domain knowledge, and preferences that AI should follow.

- Use NumPy-style docstrings for all functions and classes.
- Always check the `eed_*_utils` (e.g. ``eed_basic_utils``) packages for reusable functions before implementing new functionality.
- Always use type hints when writing new functions.
- Always add tests for new functions.
- Use `logging` for logging, not `print`.
- use `logging.getLogger(__name__)` to get the logger for the current module.
- always add loger to functions and log to trace level about the program flow
- use enumerate in for loops when you need the index
- use f-strings for string formatting
- use `Path` from `pathlib` for file and directory operations.
- Use `Path` methods like `/` for joining paths.
- Use list comprehensions for creating lists, if code remains readable.
- Use `with` statements for file operations to ensure files are properly closed.
- Use `pytest` for testing.
    - Use `pytest.mark.parametrize` for parameterized tests.
    - Ensure that all tests are run before committing code.
- use ``ruff`` for linting and formatting, see ``.pre-commit-config.yaml`` for details.
