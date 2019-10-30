import pandas as pd
import json
import requests

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

logger = log.getLogger(__name__)
formatter = log.Formatter('timestamp:%(asctime)s module:%(name)s message:%(message)s')

file_handler = log.FileHandler(__file__)
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

print(df['first digit'])