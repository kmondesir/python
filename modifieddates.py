


import logging as log
import calendar as cal
from datetime import date, timedelta

severity = {
  'CRITICAL':50,
  'ERROR':40,
  'WARNING':30,
  'INFO':20,
  'DEBUG':10,
  'NOTSET':0,
}

logger = log.getLogger(__name__)
formatter = log.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = log.FileHandler('businessdate')
file_handler.setLevel(severity['INFO'])
file_handler.setFormatter(formatter)

stream_handler = log.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

number_of_days_in_a_week = 7
number_of_days_in_a_year = 365

class returndates:
  """
  Provides various methods for manipulating and return dates, days, months, year, etc. 

  """

  minus1 = -1
  minus2 = -2
  plus1 = 1
  plus2 = 2

  def __init__(self, r_date=date.today()):
    self.weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    self.months = ("January", "February", "March", "April", "May", "June", \
      "July", "August", "September", "October", "November", "December")
    try:
      # value is expressed as an integer representing days
      self.year = r_date.year
      self.month = r_date.month - 1
      self.day = r_date.day
      self.number_of_days_in_a_month = cal.monthrange(self.year, self.month)[1]
      self.r_date = r_date
    except TypeError as e:
      logger.error(e)
    except ValueError as e:
      logger.error(e)
    except Exception as e:
      logger.error(e)
    else:
      logger.debug(self.r_date)

  def previousbusinessdate(self, value=0):
    """ Returns previous business date, skipping the weekend"""
    self.r_date = self.r_date - timedelta(days=value)

    if self.r_date.weekday() == self.weekdays.index('Saturday'):
      # subtract 1 day
      result = (self.r_date + timedelta(days=returndates.minus1)).isoformat()
      logger.debug(result)
      return result
    elif self.r_date.weekday() == self.weekdays.index('Sunday'):
      # subtract 2 days
      result = (self.r_date + timedelta(days=returndates.minus2)).isoformat()
      logger.debug(result)
      return result
    else:
      # if not a weekend then date is returned as is
      result = self.r_date.isoformat()
      logger.debug(result)
      return result

  def nextbusinessdate(self, value=0):
    """ Returns next business date, skipping the weekend"""
    self.r_date = self.r_date + timedelta(days=value)

    if self.r_date.weekday() == self.weekdays.index('Saturday'):
      # add 1 day
      result = (self.r_date + timedelta(days=returndates.plus2)).isoformat()
      logger.debug(result)
      return result
    elif self.r_date.weekday() == self.weekdays.index('Sunday'):
      # add 2 days
      result = (self.r_date + timedelta(days=returndates.plus1)).isoformat()
      logger.debug(result)
      return result
    else:
      # if not a weekend then date is returned as is
      result = self.r_date.isoformat()
      logger.debug(result)
      return result

  def weekday(self):
    """ returns a string representation of the weekday """
    result = self.weekdays[self.r_date.weekday()]
    logger.debug(result)
    return result

  def firstdateofweek(self):
    """ returns a the first date of a given week determined by the date attribute passed in """
    number_of_days_from_first_day_of_week = 0 + self.r_date.weekday()
    if self.r_date.weekday() > 0:
      result = (self.r_date - timedelta(days=number_of_days_from_first_day_of_week)).isoformat()
      logger.debug(result)
      return result
    else:
      return self.r_date.isoformat()

  def lastdateofweek(self):
    """ returns a the last date of a given week determined by the date attribute passed in """
    length = number_of_days_in_a_week - 1
    number_of_days_from_last_day_of_week = length - self.r_date.weekday()
    if self.r_date.weekday() < length:
      result = (self.r_date + timedelta(days=number_of_days_from_last_day_of_week)).isoformat()
      logger.debug(result)
      return result
    else:
      return self.r_date.isoformat()
                
  def firstdayofmonth(self):
    """ returns the first day of the month """
    result = date(self.r_date.year, self.r_date.month, 1)
    return self.weekdays[result.weekday()]

  def firstdayofyear(self):
    """ returns the first day of year """
    result = date(self.r_date.year, 1, 1).weekday()
    return self.weekdays[result]
                
  def lastdayofmonth(self):
    """ returns the last day of the month """
    result = date(self.r_date.year, self.r_date.month, self.number_of_days_in_a_month).weekday()
    return self.weekdays[result + 1]

  def lastdayofyear(self):
    """ returns the last day of the year """
    result = date(self.r_date.year,12,31).weekday()
    return self.weekdays[result]
        
  def daystoendofyear(self):
    """ returns the number of days until the end of the year """
    result = date(self.r_date.year,12,31) - self.r_date
    return result.days

  def daysfromthebeginningoftheyear(self):
    """ returns the number of days from the beginning of the year """ 
    result = date(self.r_date.year,1,1) - self.r_date 
    return abs(result.days)

  def whatmonth(self):
    """ returns full name value of the month """ 
    result = self.months[self.month]
    return result

  def whatday(self):
    """ returns full name value of the day """ 
    result = self.weekdays[self.r_date.weekday()]
    return result

  def __str__(self):
    """ returns string of r_date in iso standard format """
    return str(self.r_date.isoformat())