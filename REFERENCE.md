# Reference Materials

## Documentation

### CloudEndure

- [General Documentation](https://docs.cloudendure.com/)
- [Getting Started - API](https://docs.cloudendure.com/Content/Getting_Started_with_CloudEndure/API/API.htm)
- [REST API](https://console.cloudendure.com/api_doc/apis.html)

## API References

### Errors

Some errors are not specifically written in every method since they may always return. Those are:

- 401 (Unauthorized) - for unauthenticated requests.
- 405 (Method Not Allowed) - for using a method that is not supported (POST instead of GET).
- 403 (Forbidden) - request is authenticated, but the user is not allowed to access.
- 422 (Unprocessable Entity) - for invalid input.

## Package Related

### General Guidance

- [Python 3 - Type hints](https://docs.python.org/3/library/typing.html)
- [MyPy - Python 3 Cheat Sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

### Packages & Dependencies

#### Package Dependencies

- [Boto3 - AWS SDK](https://github.com/boto/boto3)
- [Requests - Python HTTP module](https://github.com/kennethreitz/requests)
- [Python Fire - CLI module](https://github.com/google/python-fire)

#### Build/Dev/Testing Dependencies

- [black - Python linter]()
- [isort - Python import automatic sorting]()
- [pydocstyle - Python docstring/pep-257 linting]()
- [pycodestyle - Python code complexity / McCabe validation]()
- [yapf - Python linter / automatic styling]()
- [pylint - Python linter]()
- [flake8 - Python linter]()
- [bandit]()
- [autopep8 - Python automatic styling/linting]()
- [pytest - Python test module]()
- [pytest-sugar - PyTest plugin]()
- [pytest-isort - PyTest isort plugin]()
- [coverage - Python Coverage module]()
- [codecov - CodeCov.io coverage service]()
- [pytest-cov - PyTest coverage plugin]()
- [mock - Python test mocking module]()
- [responses - Python request response testing module]()
- [twine - Python package bundling]()
- [mypy - Python type validation]()
