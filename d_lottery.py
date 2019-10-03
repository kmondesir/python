from datetime import datetime as dt
import random as rand
import statistics as stat
class winnings:
  """
  https://stackoverflow.com/questions/12906402/type-object-datetime-datetime-has-no-attribute-datetime
  """
  def __init__(self, draw_date, draw_numbers):
  
    try:  
      self.draw_date = dt.strptime(draw_date, '%m/%d/%Y')
      self.draw_numbers = list(map(int, draw_numbers.split()))
    except ValueError:
      pass
    except (TypeError, ZeroDivisionError):
      pass
    except:
      pass

  @property    
  def firstOdd(self):
    if self.draw_numbers[0] % 2 != 0:
      return True
    else:
      return False
  
  @property
  def lastOdd(self):
    if self.draw_numbers[-1] % 2 != 0:
      return True
    else:
      return False

  @property
  def isMostlyOdd(self):
    counter = 0
    for number in self.draw_numbers:
      if (number % 2 != 0):
        counter = counter + 1
    if counter > 2:
      return True
    else:
      return False

  @property
  def isMostlyEven(self):
    counter = 0
    for number in self.draw_numbers:
      if (number % 2 == 0):
        counter = counter + 1
    if counter > 2:
      return True
    else:
      return False

  @property
  def isFirstDigitSingle(self):
    if self.draw_numbers[0] < 10:
      return True  
    else:
      return False

  @property
  def isFirstDigitDouble(self):
    if self.draw_numbers[0] > 9:
      return True
    else:
      return False

  @property
  def getFirstNumber(self):
    return self.draw_numbers[0]

  @property
  def getLastNumber(self):
    return self.draw_numbers[-1]
  
  @property
  def total(self):
    return sum(self.draw_numbers)
  
  @property
  def average(self):
    return stat.mean(self.draw_number)
  
  @property
  def variance(self):
    return stat.variance(self.draw_number)
  
  @property
  def standard_deviation(self):
    return stat.stdev(self.draw_number)

  @staticmethod
  def generateRandomNumber(numbers=6,start=1,stop=59):
    seq = list(range(1,numbers))
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
