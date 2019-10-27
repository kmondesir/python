from modifieddates import returndates as rd

class holidays(rd):
  
  def __init__(self, r_date, title):
    
    super().__init__(r_date)
    
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