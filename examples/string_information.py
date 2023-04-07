from string_py import Str

random_string = Str("qOUG5p5!6wq?.s,")

print(random_string.get_upper())
# Output: ['O', 'U', 'G']

print(random_string.get_numeric(chars=False))
# Output: 3

print(random_string.get_punctuation(index=True))
# Output: {7: '!', 11: '?', 12: '.', 14: ','}
