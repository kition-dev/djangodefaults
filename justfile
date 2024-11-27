lint:
    poetry run ruff check
    poetry run ruff format
    poetry run mypy kition_djangodefaults

publish:
    poetry publish --build