"""A FizzBuzz program"""

# import necessary supporting libraries
from numbers import Number

def fizz(x):
  """
    Checks to see if the input `x` is numeric and a multiple of 3.
    If it is, it outputs 'Fizz'.
    Otherwise, it outputs the input.
  """
  return 'Fizz' if isinstance(x, Number) and x % 3 == 0 else x

def buzz(x):
  """
    Checks to see if the input `x` is numeric and a multiple of 5.
    If it is, it outputs 'Buzz'.
    Otherwise, it outputs the input.
  """
  return 'Buzz' if isinstance(x, Number) and x % 5 == 0 else x

def fibu(x):
  """
    Checks to see if the input `x` is numeric and a multiple of 15.
    If it is, it outputs 'FizzBuzz'.
    Otherwise, it outputs the input.
  """
  return 'FizzBuzz' if isinstance(x, Number) and x % 15 == 0 else x
