


import logging as log
import calendar as cal
import os
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
formatter = log.Formatter('timestamp:%(asctime)s module:%(name)s message:%(message)s')

file_handler = log.FileHandler(os.path.splitext(__file__)[0] + "." + "log")
file_handler.setLevel(severity['INFO'])
file_handler.setFormatter(formatter)

stream_handler = log.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

number_of_days_in_a_week = 7
number_of_weeks_in_a_year = 52
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
      year,week_num,dow = r_date.isocalendar()
      self.year = year
      self.month = r_date.month
      self.week = week_num
      self.day = dow - 1
      self.number_of_days_in_a_month = cal.monthrange(self.year, self.month)[1]
      self.r_date = r_date
    except TypeError as e:
      logger.error(e)
    except AttributeError as e:
      logger.error(e)
    except NameError as e:
      logger.error(e)
    except ValueError as e:
      logger.error(e)
    except Exception as e:
      logger.error(e)
    else:
      result = self.r_date
      logger.debug(result)


  def previousbusinessdate(self, value=0):
    """ Returns previous business date, skipping the weekend"""
    
    try:
      int(value) >= 0
    except TypeError as e:
      logger.error(e)
    except ValueError as e:
      logger.error(e)
    else:
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
    
    try:
      int(value) >= 0
    except TypeError as e:
      logger.error(e)
    except ValueError as e:
      logger.error(e)
    else:
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


  def firstdateofweek(self):
    """ returns a the first date of a given week determined by the date attribute passed in """
    
    number_of_days_from_first_day_of_week = self.day
    if self.day > 0:
      result = (self.r_date - timedelta(days=number_of_days_from_first_day_of_week)).isoformat()
      logger.debug(result)
      return result
    else:
      result = self.r_date.isoformat()
      logger.debug(result)
      return result


  def lastdateofweek(self):
    """ returns a the last date of a given week determined by the date attribute passed in """
    
    length = number_of_days_in_a_week
    number_of_days_from_last_day_of_week = length - self.day - 1
    if self.day < length:
      result = (self.r_date + timedelta(days=number_of_days_from_last_day_of_week)).isoformat()
      logger.debug(result)
      return result
    else:
      result = self.r_date.isoformat()
      return result

  def firstdayofmonth(self, year, month, day_of_week):
    """ returns the first day of the month 
    
      takes 1 argument for the day of the week in integer format
      
      being zero based 
      
      Monday = 0
      Tuesday = 1
      Wednesday = 2
      Thursday = 3
      Friday = 4
      Saturday = 5
      Sunday = 6
    
    """
    
    try:
      int(day_of_week) in range(0,6)
    except TypeError as e:
      logger.error(e)
    except IndexError as e:
      logger.error(e)
    except ValueError as e:
      logger.error(e)
    else:
      first_day_of_month = date(year, month, 1)
      logger.debug(first_day_of_month)
      if first_day_of_month.weekday() < day_of_week:
        difference_of_days = abs(first_day_of_month.weekday() - day_of_week)
        result = first_day_of_month + timedelta(days=difference_of_days)
        logger.debug(result)
        return result.isoformat()
      elif first_day_of_month.weekday() == day_of_week:
        return first_day_of_month.isoformat()
      else:
        difference_of_days = first_day_of_month.weekday() - day_of_week
        result = first_day_of_month + timedelta(days=number_of_days_in_a_week - difference_of_days)
        logger.debug(result)
        return result.isoformat()


  def firstdayofyear(self):
    """ returns the first day of year """
    
    result = date(self.year, 1, 1).weekday()
    logger.debug(result)
    return self.weekdays[result]

               
  def lastdayofmonth(self, year, month, day_of_week):
    """ returns the last day of the month 
    
      takes 1 argument for the day of the week in integer format
      
      being zero based e.g 
      
      Monday = 0
      Tuesday = 1
      Wednesday = 2
      Thursday = 3
      Friday = 4
      Saturday = 5
      Sunday = 6
    
    """
    
    try:
      int(day_of_week) in range(0,6)
      last_day = cal.monthrange(year, month)[1]
    except TypeError as e:
      logger.error(e)
    except ValueError as e:
      logger.error(e)
    except IndexError as e:
      logger.error(e)
    else:
      last_day_of_month = date(year, month, last_day)
      day_of_week -= 1
      logger.debug(last_day)
      if last_day_of_month.weekday() > day_of_week:
        difference_of_days = last_day_of_month.weekday() - day_of_week
        result = (last_day_of_month - timedelta(days=difference_of_days)).isoformat()
        logger.debug(result)
        return result
      elif last_day_of_month.weekday() == day_of_week:
        result = last_day_of_month.isoformat()
        logger.debug(result)
        return result
      else:
        difference_of_days = day_of_week - last_day_of_month.weekday()
        result = (last_day_of_month - timedelta(days=number_of_days_in_a_week - difference_of_days)).isoformat()
        logger.debug(result)
        return result


  def lastdayofyear(self):
    """ returns the last day of the year """
    
    result = date(self.year,12,31).weekday()
    logger.debug(result)
    return self.weekdays[result]
    
       
  def daystoendofyear(self):
    """ returns the number of days until the end of the year """
    
    result = date(self.year,12,31) - self.r_date
    logger.debug(result)
    return result.days


  def daysfromthebeginningoftheyear(self):
    """ returns the number of days from the beginning of the year """ 
    
    result = date(self.year,1,1) - self.r_date
    logger.debug(result)
    return abs(result.days)
  
  
  def whatyear(self):
    """ returns the year associated with the date provided """
    
    result = self.year
    logger.debug(result)
    return result


  def whatmonth(self):
    """ returns full name value of the month """ 
    
    result = self.months[self.month]
    logger.debug(result)
    return result


  def whatday(self):
    """ returns day number for the year """ 
    
    result = date(self.year,1,1) - self.r_date 
    logger.debug(result)
    return abs(result.days) + 1


  def whatdayofweek(self):
    """ returns the full name of the day of the week """
    
    result = self.weekdays[self.day]
    logger.debug(result)
    return result


  def whatweek(self):
    """ returns the week number of the year """
    
    result = self.week
    logger.debug(result)
    return result


  @staticmethod
  def yesterday():
    """ returns the day before today """
    
    result = date.today() - timedelta(days=1)
    logger.debug(result)
    return result.isoformat()


  @staticmethod
  def tomorrow():
    """ returns the day after today """
    
    result = date.today() + timedelta(days=1)
    logger.debug(result)
    return result.isoformat()


  def __str__(self):
    """ returns string of r_date in iso standard format """
    
    result = self.r_date.isoformat()
    logger.debug(result)
    return result


  def __repr__(self):
    """ Doesn't work but might be cool """
    
    result = "{}(date({},{},{}))".format(self.__class__.__name__,self.year, self.month, self.day) 
    logger.debug(result)
    return result