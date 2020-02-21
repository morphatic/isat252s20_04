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

    def throws_an_error_if_fizz_has_no_input():
      """Makes sure fizz() throws an error if there is no input"""
      with raises(Exception) as err_info:
        fizz() # pylint: disable=no-value-for-parameter
      assert err_info.type == TypeError
      assert 'missing 1 required positional argument' in str(err_info.value)

    def outputs_fizz_if_an_input_is_numeric_and_a_multiple_of_3():
      """
        Checks to see if the input `x` is numeric and a multiple of 3.
        If it is, it outputs 'fizz'.
        Otherwise, it outputs the input.
      """
      assert fizz(3) == 'fizz'      # multiple of 3
      assert fizz(4) == 4           # non-multiple of 3
      assert fizz(0) == 'fizz'      # zero
      assert fizz(15) == 'fizz'     # multiple of 3 and 5
      assert fizz(-3) == 'fizz'     # negative multiple of 3
      assert fizz(-2) == -2         # negative non-multiple of 3
      assert fizz(3.5) == 3.5       # non-integer
      assert fizz('buzz') == 'buzz' # non-numeric
