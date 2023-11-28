def add_numbers(a, b):
    return a + b

assert add_numbers(1, 2) == 3

# SHould hive an error
has_raised_error = False
try:
    add_numbers("nonsense", "irrelevant")
except AssertionError:
    has_raised_error = True
assert has_raised_error