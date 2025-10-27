1. \Which issues were easiest to fix, and which were hardest?

The easiest were style and naming errors (Flake8 and Pylint gave clear suggestions).

The hardest was removing eval() safely and replacing it while preserving functionality.

2. Did the static analysis tools report any false positives?

Pylint reported some minor naming issues for intentionally short helper functions, which weren’t truly problems, but I fixed them anyway.

3. How would you integrate these tools into your workflow?

I’d add them to a GitHub Actions workflow so every commit automatically runs Pylint, Bandit, and Flake8.

I’d also set up pre-commit hooks to catch issues before pushing code.

4. What improvements did you observe after fixing issues?

The code is now cleaner, documented, and secure.

File operations are safer, logging works properly, and Pylint rated it 10/10 — proving real improvement in maintainability.