# string_py


[![PyPI](https://img.shields.io/pypi/v/string-py?style=flat-square)](https://pypi.org/project/string-py/)

A Python package to simplify working with strings

## Installation

To install the library directly from PyPI you can just run the following command:
```shell
# Linux/macOS
python3 -m pip install -U string-py

# Windows
py -3 -m pip install -U string-py
```


## Format Example

```python
from string_py import Format

print(Format.align(values={"Username:": "John", "Register Date:": "01.01.2001"}))
```
```
Username:        John
Register Date:   01.01.2001
```
## Manipulation Example
```python
from string_py import Str

print(Str("Hello World!").first(5))
```
```
Hello
```
## Information Example
```python
from string_py import Str

print(Str("Hello World!").get_upper(index=True))
```
```
{0: 'H', 6: 'W'}
```
## Printer Example
```python
from string_py import Printer

print = Printer()

print.time("Hello World!")
```
```
[04.04 | 03:11:07] Hello World!
```
