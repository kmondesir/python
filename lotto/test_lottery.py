import unittest
from lottery import lotto

class test_lotto(unittest.TestCase):

  def test_first_digit(self):
    control = 6
    result = lotto('6 11 19 21 32').getFirstNumber()
    msg = "{} is different from {}".format(result, control)
    self.assertEqual(result, control, msg)

  def test_last_digit(self):
    control = 32
    result = lotto('6 11 19 21 32').getLastNumber()
    msg = "{} is different from {}".format(result, control)
    self.assertEqual(result, control, msg)

  def test_total(self):
    control = 89
    result = lotto('6 11 19 21 32').total()
    msg = "{} is different from {}".format(result, control)
    self.assertEqual(result, control, msg)

  def test_average(self):
    control = 17.8
    result = lotto('6 11 19 21 32').average()
    msg = "{} is different from {}".format(result, control)
    self.assertEqual(result, control, msg)

  def test_is_first_digit_single(self):
    result = lotto('6 11 19 21 32').isFirstDigitSingle()
    self.assertTrue(result)

  def test_is_last_digit_single(self):
    result = lotto('10 11 19 21 32').isFirstDigitDouble()
    self.assertTrue(result)