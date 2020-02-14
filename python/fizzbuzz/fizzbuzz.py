"""A FizzBuzz program"""

# import necessary supportin libraries
from numbers import Number

def fizz(x):
  """Checks to see if the input is a multiple of 3"""
  # check to see if the input is a number
  if isinstance(x, Number):
    # why yes, it is a number
    return x % 3 == 0
  else:
    # nope, it is NOT a number
    return False