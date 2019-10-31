from calculateddates import returndates as rd
import datetime as dt

class holidays(rd):
  
  def __init__(self, title, r_date):
    
    super().__init__(r_date)
    self.title = title
    self.us = {
      'New Years':dt.datetime.date(self.whatyear(),1,1),
      'Martin Luther King':0,
      'Memorial':0,
      'Independence':dt.datetime.date(self.whatyear(),7,4),
      'Labor': dt.datetime.strftime(self.firstdayofmonth(0)),
      'Veterans':0,
      'Thanksgiving':dt.datetime.strftime(self.lastdayofmonth(3)),
      'Christmas':dt.datetime.date(self.las,12,25)
    }
    
  def new_date(self):
    result = self.us[self.title]
    return result
