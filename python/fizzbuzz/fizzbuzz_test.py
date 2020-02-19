# pylint: disable=unused-variable
"""Unit tests for FizzBuzz."""

# import the code to be tested
from fizzbuzz import fizz

# import utilities for writing tests
from pytest import raises

def describe_a_fizzbuzz_program_that():
  """A program to play the FizzBuzz game."""

  def has_a_smoke_test():
    """Make sure our testing infrastructure is working."""
    assert True == True

  def describes_a_fizz_function_that():

    def throws_an_error_if_fizz_input_is_not_a_positive_integer_or_text():
      """Make sure input to fizz()is positive integer or text"""
      with raises(TypeError) as err_info:
        fizz() # pylint: disable=no-value-for-parameter

    # def can_indicate_if_a_number_is_a_multiple_of_3():
    #   """Checks to see if a number is a multiple of 3"""
    #   assert fizz(3) == True       # multiple of 3
    #   assert fizz(4) == False      # non-multiple of 3
    #   assert fizz(0) == True       # zero
    #   assert fizz(15) == True      # multiple of 3 and 5
    #   assert fizz(-3) == True      # negative multiple of 3
    #   assert fizz(-2) == False     # negative non-multiple of 3
    #   assert fizz(3.5) == False    # non-integer
    #   assert fizz('buzz') == False # non-numeric
    #   assert fizz() == False       # no input
