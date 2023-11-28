def add_numbers(a, b):
    """Adds two numbers."""
    assert isinstance(a, (int, float)), "a must be an integer"
    assert isinstance(b, (int, float)), "b must be an integer"
    return a + b

assert add_numbers(1, 2) == 3

has_raised_error = False
try:
    add_numbers("nonsense", "irrelevant")
except AssertionError:
    has_raised_error = True
assert has_raised_error

assert add_numbers.__doc__
