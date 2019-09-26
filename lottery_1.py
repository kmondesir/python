import pandas as pd
import os
import array as arr
from d_lottery import winnings as wins

path = os.getcwd()
item = 'Lottery_NY_Lotto_Winning_Numbers__Beginning_2001.csv'

COLS_TO_USE = ['Draw Date', 'Winning Numbers']

print(path)

CSV_PATH = os.path.join(path,item)

print(CSV_PATH)

df = pd.read_csv(CSV_PATH, usecols=COLS_TO_USE)

print(df)

#print(df.loc['09/11/2019', 'Winning Numbers'])

win = []

for index, row in df.iterrows():
  print(index, row)
  win.append(wins(df.loc[index, 'Draw Date'], df.loc[index, 'Winning Numbers']))

wins.generateRandomNumber()

print (str(win[0].draw_date))
"""
df['Draw Date'] = pd.to_datetime(df['Draw Date'], errors='coerce', format="%m/%d/%Y")

df['Winning Numbers'] = df['Winning Numbers'].apply(lambda x : x.split()) # Converts string into a list of strings

df['Winning Numbers'] = df['Winning Numbers'].apply(lambda x : list(map(int,x))) # Converts list of strings to list of ints
"""
