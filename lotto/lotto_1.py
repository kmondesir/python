
import pandas as pd
import os

from lottery import lotto as t5

import logging as log
severity = {
            'CRITICAL': 50,
            'ERROR': 40,
            'WARNING': 30,
            'INFO': 20,
            'DEBUG': 10,
            'NOTSET': 0,
}

logger = log.getLogger(__name__)
formatter = log.Formatter('timestamp:%(asctime)s module:%(name)s message:%(message)s')

file_handler = log.FileHandler(__file__)
file_handler.setLevel(severity['INFO'])
file_handler.setFormatter(formatter)

stream_handler = log.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# url = 'https://data.ny.gov/api/odata/v4/dg63-4siq'
# service = od(url, reflect_entities=True)

path = os.getcwd()
print(path)
item = 'Lottery_Take_5_Winning_Numbers.csv'

print(item)
ABS_PATH = os.path.join(path, item)
print(ABS_PATH)

columns = ['Draw Date', 'Winning Numbers']

df = pd.read_csv(ABS_PATH, usecols=columns)
# items = service.entities['Draw Date']

# query = service.query(items)



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
  numbers.append(t5(str(row['Winning Numbers']),str(row['Draw Date'])))

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

def generateRandomList(lower=84, upper=115):
  result = list()
  counter = 0
  while sum(result).__le__(lower) or sum(result).__ge__(upper):
    counter += 1
    result = t5.generateRandomNumber(5,1,39)
  else:
    return result
 
global new_numbers
new_numbers = list()

global counter
counter = 0

while counter < 20:
  result = generateRandomList() 
  if result not in list(df['Winning Numbers']):
    new_numbers.append(result)
    counter += 1
  else:
    continue

  print(new_numbers)