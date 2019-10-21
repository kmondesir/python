



import logging as log
import random as rand
import statistics as stat
from datetime import datetime as dt

severity = {
    'CRITICAL': 50,
    'ERROR': 40,
    'WARNING': 30,
    'INFO': 20,
    'DEBUG': 10,
    'NOTSET': 0,
}

logger = log.getLogger(__name__)
formatter = log.Formatter(
    'timestamp:%(asctime)s module:%(name)s message:%(message)s')

file_handler = log.FileHandler(__file__)
file_handler.setLevel(severity['INFO'])
file_handler.setFormatter(formatter)

stream_handler = log.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
class winnings:
  """
  Performs various calculates on a series of numbers

  https://stackoverflow.com/questions/12906402/type-object-datetime-datetime-has-no-attribute-datetime
  """
  def __init__(self, draw_date, draw_numbers):
  
    try:  
      self.draw_date = dt.strptime(draw_date, '%m/%d/%Y')
      self.draw_numbers = list(map(int, draw_numbers.split()))
    except TypeError as e:
      logger.error(e)
    except ValueError as e:
      logger.error(e)
    except NameError as e:
      logger.error(e)
    except Exception as e:
      logger.error(e)
    else:
      logger.debug(self.draw_date)
      logger.debug(self.draw_numbers)
    
  def firstOdd(self):
    # Returns True if the first digit is odd
    if self.draw_numbers[0] % 2 != 0:
      return True
    else:
      return False
  
  def lastOdd(self):
    # Returns True if the last digit is odd 
    if self.draw_numbers[-1] % 2 != 0:
      return True
    else:
      return False

  def isMostlyOdd(self):
    # Returns True if more than half of the values are odd
    counter = 0
    for number in self.draw_numbers:
      if (number % 2 != 0):
        counter = counter + 1
    if counter > len(self.draw_numbers)/2:
      return True
    else:
      return False

  def isMostlyEven(self):
    # Returns True if more than half of the values are even
    counter = 0
    for number in self.draw_numbers:
      if (number % 2 == 0):
        counter = counter + 1
    if counter > len(self.draw_numbers)/2:
      return True
    else:
      return False

  def isFirstDigitSingle(self):
    # Returns True if the first digit is less than 10
    if self.draw_numbers[0] < 10:
      return True  
    else:
      return False

  def isFirstDigitDouble(self):
    # Returns True if the first digit is greater than 9
    if self.draw_numbers[0] > 9:
      return True
    else:
      return False

  def getFirstNumber(self):
    # Returns the first number in a sequence
    return self.draw_numbers[0]

  def getLastNumber(self):
    # Returns the last number in a sequence
    return self.draw_numbers[-1]
  
  def total(self):
    # Returns the sum of all values in the sequence
    return sum(self.draw_numbers)
  
  def average(self):
    # Returns the average of all values in the sequence
    return stat.mean(self.draw_numbers)
  
  def variance(self):
    # Returns the variance of all values in the sequence
    return stat.variance(self.draw_numbers)
  
  def standard_deviation(self):
    # Returns the standard deviation of all values in the sequence
    return stat.stdev(self.draw_numbers)

  @staticmethod
  def generateRandomNumber(numbers=6,start=1,stop=59):
    """ Generates random numbers based on three arguments
      numbers: length of series

      start: start of range

      stop: end of range
    """
    seq = list(range(numbers))
    first = rand.randrange(1,9)
    seq[0] = first
    last = rand.randrange(40,stop)
    seq[-1] = last

    counter = 1
    while counter < (numbers - 1):
      item = rand.randrange(first, last)
      if (item == first) or (item == last):
        pass
      elif item in seq:
        pass
      else:
        seq[counter] = item
        counter += 1
    return sorted(seq)

  @staticmethod
  def generateRandomList(lower=30, upper=100):
    result = list()
    counter = 0
    while sum(result).__le__(lower) or sum(result).__ge__(upper):
      counter += 1
      result = winnings.generateRandomNumber()
    else:
      return result
