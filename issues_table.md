cat > issues_table.md <<'EOF'
# Issues Fixed (Static Code Analysis)

| Issue Type              | Tool     | Lines (original) | Description                                           | Fix Approach                                                       |
|-------------------------|----------|------------------|-------------------------------------------------------|--------------------------------------------------------------------|
| Mutable default arg     | Pylint   | 8                | `logs=[]` shared across calls                         | Changed to `logs=None` and initialized inside the function.        |
| Bare except / pass      | Pylint + Bandit | 19         | `except:` hides all exceptions (B110)                 | Replaced with `except KeyError:` and logged a warning.             |
| Insecure `eval()`       | Bandit   | 59               | Use of `eval()` (B307)                                | Removed `eval()` entirely (no unsafe execution).                   |
| File handling & encoding| Pylint   | 26, 32           | `open()` without context manager/encoding             | Used `with open(..., encoding="utf-8")` for load/save.             |
| Naming conventions      | Pylint   | multiple         | camelCase function names (`addItem`, etc.)            | Renamed to snake_case (`add_item`, `remove_item`, etc.).           |
| Missing docstrings      | Pylint   | multiple         | Module and functions lacked docstrings                | Added module/function docstrings describing behavior.              |
| Unused import           | Flake8   | 2                | `logging` imported but unused                         | Configured and used `logging` for info/warn/error messages.        |
| String formatting style | Pylint   | 12               | `%` formatting where f-strings recommended (C0209)    | Replaced with f-strings / logging parameterized messages.          |
