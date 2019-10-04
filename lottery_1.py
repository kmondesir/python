import pandas as pd
import os
from lottery import winnings as wins

path = os.getcwd()
print(path)
item = 'Lottery_Take_5_Winning_Numbers.csv'

print(item)
ABS_PATH = os.path.join(path, item)
print(ABS_PATH)

columns = ['Draw Date', 'Winning Numbers']

df = pd.read_csv(ABS_PATH, usecols=columns)

global numbers

numbers = []

global firstDigit
global lastDigit

firstDigit = []
lastDigit = []

global firstOdd
global lastOdd

firstOdd = []
lastOdd = []

global singleDigit
global doubleDigit

singleDigit = []
doubleDigit = []

global mostlyOdd

mostlyOdd = []

global total
global average
global standard_d
global variance

total = []
average = []
standard_d = []
variance = []

for index, row in df.iterrows():
  numbers.append(wins(str(row['Draw Date']),str(row['Winning Numbers'])))

for i in numbers:

  firstDigit.append(i.getFirstNumber())
  lastDigit.append(i.getLastNumber())

  firstOdd.append(i.firstOdd())
  lastOdd.append(i.lastOdd())
  mostlyOdd.append(i.isMostlyOdd())
  singleDigit.append(i.isFirstDigitSingle())
  doubleDigit.append(i.isFirstDigitDouble())

  total.append(i.total())
  average.append(i.average())
  standard_d.append(i.standard_deviation())
  variance.append(i.variance())

print(variance[0])

df['first digit'] = firstDigit
df['last digit'] = lastDigit

df['first odd digit'] = firstOdd
df['last odd digit'] = lastOdd
df['mostly odd'] = mostlyOdd
df['first digit less than 10'] = singleDigit
df['first digit greater than 9'] = doubleDigit

df['sum'] = total
df['average'] = average
df['standard_d'] = standard_d
df['variance'] = variance

df.to_pickle('nytake5.pkl')
