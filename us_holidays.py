from modifieddates import returndates as rd
from datetime import date, timedelta

def __init__(self, year=date.year()):
    self.year = year
    self.holidays = {'New Years':date(year,1,1),
    'Martin Luther King':(rd.lastdayofmonth(0) - timedelta(days=7)), 
    'Memorial':rd.lastdayofmonth(0),
    'Independence':date(year,7,4),
    'Labor':rd.firstdayofmonth(0),
    'Veterans':(rd.firstdayofmonth(0) + timedelta(days=7)),
    'Thankgiving':rd.lastdayofmonth(3),
    'Christmas':date(year,12,25)}

@property
def new_years(self):
    return self.holidays['New Years']