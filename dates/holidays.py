from python.dates.calculateddates import returndates as rd
import datetime as dt

class holidays(rd):
  
  def __init__(self, r_date, title):
    
    super().__init__(r_date)
    self.title = title
    self.us = {
      'New Years':0,
      'Martin Luther King':0,
      'Memorial':0,
      'Independence':0,
      'Labor':0,
      'Veterans':0,
      'Thanksgiving':0,
      'Christmas':0
    }
    
  def new_date(self, holiday):
    result = self.us[holiday]
    return result