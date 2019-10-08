from datetime import date, timedelta

class returndate:

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
      self.value = value
      if value is None:
        self.r_date = r_date
      else:
        self.r_date = r_date + timedelta(days=self.value) 
    except:
      pass

  def previousbusinessdate(self):
    
    if self.r_date.weekday() == returndate.weekdays.index('Saturday'):
      #subtract 1 day
      return (self.r_date + timedelta(days=returndate.minus1)).isoformat()
    elif self.r_date.weekday() == returndate.weekdays.index('Sunday'):
      #subtract 2 days
      return (self.r_date + timedelta(days=returndate.minus2)).isoformat()
    else:
      return self.r_date.isoformat()

  def nextbusinessdate(self):
  
    if self.r_date.weekday() == returndate.weekdays.index('Saturday') :
      #add 1 day
      return (self.r_date.weekday() + timedelta(days=returndate.plus2)).isoformat()
    elif self.r_date.weekday() == returndate.weekdays.index('Sunday'):
      #add 2 days
      return (self.r_date.weekday() + timedelta(days=returndate.plus1)).isoformat()
    else:
      return self.r_date.isoformat()
