from datetime import date, timedelta

class returndate:
  """ Returns calculated date by adding or subtracting days """

  weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  minus1 = -1
  minus2 = -2
  minus3 = -3
  minus4 = -4
  minus5 = -5
  plus1 = 1
  plus2 = 2
  plus3 = 3
  plus4 = 4
  plus5 = 5

  def __init__(self, r_date=date.today(), value=None):
    try:
      self.r_date = r_date
      #expressed as days
      self.value = int(value)
      if value is None:
        pass
      elif value not in range(0,4):
        raise ValueError(self.value)
      else:
        self.r_date = r_date + timedelta(days=self.value) 
    except TypeError as e:
      print(e)
    except Exception as e:
      print(e)

  def previousbusinessdate(self):
    """ Returns previous business date, skipping the weekend"""
    
    if self.r_date.weekday() == returndate.weekdays.index('Saturday'):
      #subtract 1 day
      return (self.r_date + timedelta(days=returndate.minus1)).isoformat()
    elif self.r_date.weekday() == returndate.weekdays.index('Sunday'):
      #subtract 2 days
      return (self.r_date + timedelta(days=returndate.minus2)).isoformat()
    else:
      return self.r_date.isoformat()

  def nextbusinessdate(self):
    """ Returns next business date, skipping the weekend"""

    if self.r_date.weekday() == returndate.weekdays.index('Saturday') :
      #add 1 day
      return (self.r_date.weekday() + timedelta(days=returndate.plus2)).isoformat()
    elif self.r_date.weekday() == returndate.weekdays.index('Sunday'):
      #add 2 days
      return (self.r_date.weekday() + timedelta(days=returndate.plus1)).isoformat()
    else:
      return self.r_date.isoformat()

  def __str__(self):
    return str(self.r_date.isoformat())
