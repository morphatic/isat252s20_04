"""A FizzBuzz program"""

# import necessary supportin libraries
from numbers import Number

def fizz(x):
  """
    Checks to see if the input `x` is numeric and a multiple of 3.
    If it is, it outputs 'fizz'.
    Otherwise, it outputs the input.
  """
  if isinstance(x, Number) and x % 3 == 0:
    return 'fizz'
  else:
    return x