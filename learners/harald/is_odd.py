def is_even(value):
    """checks if value is an even integer"""
    if not(isinstance(value, int)):
        raise AssertionError

    if value%2 == 0:
        return True
    else:
        return False


#test
assert is_even(0)
assert is_even(1) == False
assert is_even.__doc__


has_given_exception = False
try:    
    is_even("wefufewpf")
except AssertionError:    
    has_given_exception = True
assert has_given_exception
