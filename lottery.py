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
    except TypeError:
      print("Type entered not expected, please use strings")
    except ValueError:
      print("Value entered not expected")
    except NameError:
      print("Name error")
    except:
      print("Unexpected error")
    
  def firstOdd(self):
    if self.draw_numbers[0] % 2 != 0:
      return True
    else:
      return False
  
  def lastOdd(self):
    if self.draw_numbers[-1] % 2 != 0:
      return True
    else:
      return False

  def isMostlyOdd(self):
    counter = 0
    for number in self.draw_numbers:
      if (number % 2 != 0):
        counter = counter + 1
    if counter > 2:
      return True
    else:
      return False

  def isMostlyEven(self):
    counter = 0
    for number in self.draw_numbers:
      if (number % 2 == 0):
        counter = counter + 1
    if counter > 2:
      return True
    else:
      return False

  def isFirstDigitSingle(self):
    if self.draw_numbers[0] < 10:
      return True  
    else:
      return False

  def isFirstDigitDouble(self):
    if self.draw_numbers[0] > 9:
      return True
    else:
      return False

  def getFirstNumber(self):
    return self.draw_numbers[0]

  def getLastNumber(self):
    return self.draw_numbers[-1]
  
  def total(self):
    return sum(self.draw_numbers)
  
  def average(self):
    return stat.mean(self.draw_numbers)
  
  def variance(self):
    return stat.variance(self.draw_numbers)
  
  def standard_deviation(self):
    return stat.stdev(self.draw_numbers)

  @staticmethod
  def generateRandomNumber(numbers=5,start=1,stop=39):
    seq = list(range(numbers))
    first = rand.randrange(start, 9)
    seq[0] = first
    last = rand.randrange(30, stop)
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
      result = generateRandomNumber()
    else:
      return result
