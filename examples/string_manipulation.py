from string_py import Str
import string

# Generate
print(Str("".join(string.ascii_lowercase + string.ascii_uppercase + string.digits)).generate(length=10))
# Output Example: 741P4MBHc5

# Split
print(Str("Hello World!").split(each=3))
# Output: ['Hel', 'lo ', 'Wor', 'ld!']
print(Str("Hello World!").split(chars=" "))
# Output: ['Hello', 'World!']

# First and Last
print(Str("Hello World!").first())
# Output: H
print(Str("Hello World!").first(5))
# Output: Hello
print(Str("Hello World!").first(5, remove=True))
# Output: World!
print(Str("Hello World!").last())
# Output: !
print(Str("Hello World!").last(5))
# Output: World!
print(Str("Hello World!").last(5, remove=True))
# Output: Hello
