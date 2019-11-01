from calculateddates import returndates as rd
import datetime as dt

class holidays(rd):
  
  def __init__(self, title, year, r_date):
    
    super().__init__(r_date)
    self.title = title
    self.us = {
      'New Years':dt.datetime.date(year,0,1),
      'Martin Luther King': dt.datetime.strftime(self.lastdayofmonth(year, 0, 0) - dt.timedelta(days=7)),
      'Memorial': dt.datetime.strftime(self.lastdayofmonth(year, 4, 0)),
      'Independence':dt.datetime.date(year,6,4),
      'Labor': dt.datetime.strftime(self.firstdayofmonth(year,8,0)),
      'Veterans': dt.datetime.strftime(self.firstdayofmonth(year, 10, 0) + dt.timedelta(days=7)),
      'Thanksgiving':dt.datetime.strftime(self.lastdayofmonth(year,10,3)),
      'Christmas':dt.datetime.date(year,11,25)
    }
    
  def new_date(self):
    result = self.us[self.title]
    return result