---
applyTo: '**/*.py'
---
Coding standards, domain knowledge, and preferences for AI to follow:

- Write all function and class docstrings in NumPy style.
- Before implementing new features, check the `eed_*_utils` packages (e.g., `eed_basic_utils`) for reusable code.
- Always include type hints in new functions.
- Add tests for every new function.
- Use the `logging` module instead of `print` statements.
- Obtain the logger with `logging.getLogger(__name__)` in each module.
- Add a logger to functions and use trace-level logging to track program flow.
- Use `enumerate` in loops when the index is needed.
- Prefer f-strings for formatting strings.
- Use `Path` from `pathlib` for file and directory operations.
- Join paths using the `/` operator with `Path`.
- Favor list comprehensions for list creation when readability is maintained.
- Use `with` statements for file operations to ensure proper closure.
- Use `pytest` for testing:
    - Apply `pytest.mark.parametrize` for parameterized tests.
    - Run all tests before committing code.
- Use `ruff` for linting and formatting; refer to `.pre-commit-config.yaml` for configuration.
