



import logging as log
from datetime import date, timedelta

weekdays = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]

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

class returndate:
  """ Returns calculated date by adding or subtracting days """

  minus1 = -1
  minus2 = -2
  plus1 = 1
  plus2 = 2

  def __init__(self, r_date=date.today(), value=None):
    try:
      # value is expressed as an integer representing days
      if value is None:
        self.r_date = r_date
      else:
        self.value = int(value)
    except TypeError as e:
      logger.error(e)
    except ValueError as e:
      logger.error(e)
    except Exception as e:
      logger.error(e)
    else:
      self.r_date = r_date + timedelta(days=self.value)
      logger.debug(self.r_date)

  def previousbusinessdate(self):
    """ Returns previous business date, skipping the weekend"""
    
    if self.r_date.weekday() == weekdays.index('Saturday'):
      # subtract 1 day
      result = (self.r_date + timedelta(days=returndate.minus1)).isoformat()
      logger.debug(result)
      return result
    elif self.r_date.weekday() == weekdays.index('Sunday'):
      # subtract 2 days
      result = (self.r_date + timedelta(days=returndate.minus2)).isoformat()
      logger.debug(result)
      return result
    else:
      # if not a weekend then date is returned as is
      result = self.r_date.isoformat()
      logger.debug(result)
      return result

  def nextbusinessdate(self):
    """ Returns next business date, skipping the weekend"""

    if self.r_date.weekday() == weekdays.index('Saturday') :
      # add 1 day
      result = (self.r_date.weekday() + timedelta(days=returndate.plus2)).isoformat()
      logger.debug(result)
      return result
    elif self.r_date.weekday() == weekdays.index('Sunday'):
      # add 2 days
      result = (self.r_date.weekday() + timedelta(days=returndate.plus1)).isoformat()
      logger.debug(result)
      return result
    else:
      # if not a weekend then date is returned as is
      result = self.r_date.isoformat()
      logger.debug(result)
      return result

  def __str__(self):
    return str(self.r_date.isoformat())
