# pytest-monkeytype

[![Build Status](https://travis-ci.org/mariusvniekerk/pytest-monkeytype.svg?branch=master)](https://travis-ci.org/mariusvniekerk/pytest-monkeytype)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPI Python](https://img.shields.io/pypi/pyversions/pytest-monkeytype.svg)](https://pypi.python.org/pypi/pytest-monkeytype)
[![PyPI Version](https://img.shields.io/pypi/v/pytest-monkeytype.svg)](https://pypi.python.org/pypi/pytest-monkeytype)
[![PyPI Status](https://img.shields.io/pypi/status/pytest-monkeytype.svg)](https://pypi.python.org/pypi/pytest-monkeytype)
[![PyPI Wheel](https://img.shields.io/pypi/wheel/pytest-monkeytype.svg)](https://pypi.python.org/pypi/pytest-monkeytype)


[MonkeyType](https://github.com/Instagram/MonkeyType) as a
[pytest](https://docs.pytest.org/en/latest/) plugin.

```
pip install pytest-monkeytype

# Generate annotations by running your pytest tests as usual:
py.test --monkeytype-output=./monkeytype.sqlite3

# Get a listing of modules annotated by monkeytype
monkeytype list-modules 

# Generate a stub file for those annotations using monkeytype:
monkeytype stub some.module

# Apply these annotations directly
monkeytype apply some.module
```


This project is inspired by [pytest-annotate](https://github.com/kensho-technologies/pytest-annotate)