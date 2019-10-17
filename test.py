import modifieddates as md
from datetime import date

result = md.returndates()

# help(result)

print(result.daysfromthebeginningoftheyear())

print(result.daystoendofyear())

print(result.firstdateofweek())

print(result.lastdateofweek())

print(result.firstdayofmonth())

print(result.lastdayofmonth())

print(result.whatday())

print(result.whatdayofweek())

print(result.whatweek())