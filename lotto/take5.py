import pandas as pd
import json
import requests
import datetime as dt
import os

from lottery import lotto as take5

import logging as log
severity = {
            'CRITICAL': 50,
            'ERROR': 40,
            'WARNING': 30,
            'INFO': 20,
            'DEBUG': 10,
            'NOTSET': 0,
}
thisfile = __file__
logger = log.getLogger(__name__)
formatter = log.Formatter('timestamp:%(asctime)s module:%(name)s message:%(message)s')

file_handler = log.FileHandler('take5.log')
file_handler.setLevel(severity["INFO"])
file_handler.setFormatter(formatter)

stream_handler = log.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


response = requests.get("https://data.ny.gov/api/odata/v4/dg63-4siq")
converted = json.loads(response.content)
df = pd.DataFrame.from_dict(converted['value'], orient='columns')

df['first digit'] = list(map(lambda x: take5(x).getFirstNumber(), df['winning_numbers']))
df['last digit'] = list(map(lambda x: take5(x).getLastNumber(), df['winning_numbers']))

df['first odd digit'] = list(map(lambda x: take5(x).firstOdd(), df['winning_numbers']))
df['last odd digit'] = list(map(lambda x: take5(
    x).lastOdd(), df['winning_numbers']))
df['mostly odd'] = list(map(lambda x: take5(x).isMostlyOdd, df['winning_numbers']))
df['first digit less than 10'] = list(map(lambda x: take5(x).isFirstDigitSingle(), df['winning_numbers']))
df['first digit greater than 9'] = list(map(lambda x: take5(x).isFirstDigitDouble(), df['winning_numbers']))

df['sum'] = list(map(lambda x: take5(x).total(), df['winning_numbers']))
df['average'] = list(map(lambda x: take5(x).average(), df['winning_numbers']))
df['standard_d'] = list(map(lambda x: take5(x).standard_deviation(), df['winning_numbers']))
df['variance'] = list(map(lambda x: take5(x).variance(), df['winning_numbers']))

print(df)