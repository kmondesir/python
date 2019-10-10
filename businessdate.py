
from datetime import date, timedelta

weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

class returndate:
  """ Returns calculated date by adding or subtracting days """

  minus1 = -1
  minus2 = -2
  plus1 = 1
  plus2 = 2

  def __init__(self, r_date=date.today(), value=None):
    try:
      #expressed as days
      if value is None:
        self.r_date = r_date
      else:
        self.value = int(value)
    except TypeError as e:
      print(e)
    except ValueError as e:
      print(e)
    except Exception as e:
      print(e)
    else:
      self.r_date = r_date + timedelta(days=self.value)

  def previousbusinessdate(self):
    """ Returns previous business date, skipping the weekend"""
    
    if self.r_date.weekday() == weekdays.index('Saturday'):
      #subtract 1 day
      return (self.r_date + timedelta(days=returndate.minus1)).isoformat()
    elif self.r_date.weekday() == weekdays.index('Sunday'):
      #subtract 2 days
      return (self.r_date + timedelta(days=returndate.minus2)).isoformat()
    else:
      return self.r_date.isoformat()

  def nextbusinessdate(self):
    """ Returns next business date, skipping the weekend"""

    if self.r_date.weekday() == weekdays.index('Saturday') :
      #add 1 day
      return (self.r_date.weekday() + timedelta(days=returndate.plus2)).isoformat()
    elif self.r_date.weekday() == weekdays.index('Sunday'):
      #add 2 days
      return (self.r_date.weekday() + timedelta(days=returndate.plus1)).isoformat()
    else:
      return self.r_date.isoformat()

  def __str__(self):
    return str(self.r_date.isoformat())
