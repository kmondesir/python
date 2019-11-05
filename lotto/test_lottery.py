import unittest
from lottery import lotto

class test_lotto(unittest.TestCase):

  def test_first_digit(self):
    # test first digit against the control
    control = 6
    result = lotto('6 11 19 21 32').getFirstNumber()
    msg = "{} does not equal {}".format(result, control)
    self.assertEqual(result, control, msg)

  def test_last_digit(self):
    # test last digit against the control
    control = 32
    result = lotto('6 11 19 21 32').getLastNumber()
    msg = "{} does not equal {}".format(result, control)
    self.assertEqual(result, control, msg)

  def test_total(self):
    # test the sum against the control
    control = 89
    result = lotto('6 11 19 21 32').total()
    msg = "{} does not equal {}".format(result, control)
    self.assertEqual(result, control, msg)

  def test_average(self):
    # test the average against the control
    control = 17.8
    result = lotto('6 11 19 21 32').average()
    msg = "{} does not equal {}".format(result, control)
    self.assertEqual(result, control, msg)

  def test_is_first_digit_single(self):
    # test the first digit is single
    result = lotto('6 11 19 21 32').isFirstDigitSingle()
    msg = "result is not true"
    self.assertTrue(result, msg)

  def test_is_first_digit_double(self):
    # test the first digit is double
    result = lotto('10 11 19 21 32').isFirstDigitDouble()
    msg = "result is not true"
    self.assertTrue(result, msg)

  def test_mostly_odd(self):
    # test if list is mostly odd
    result = lotto('9 10 17 23 39').isMostlyOdd()
    msg = "result is not true"
    self.assertTrue(result, msg)

  def test_first_odd(self):
    # test if the first odd
    result = lotto('9 10 17 23 39').firstOdd()
    msg = "result is not true"
    self.assertTrue(result, msg)