


import sys
import os
import pyodbc
import pandas as pd


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
formatter = log.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = log.FileHandler("utilities.py")
file_handler.setLevel(severity["DEBUG"])
file_handler.setFormatter(formatter)

stream_handler = log.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

class querying:

  """
  Creates a connection string and provides CRUD methods for data manipulation

  This video demostrates how to connect to SQL with Python using the pyodbc class, 
  this may not be the best way to connect but its the simplest to understand

  https://www.youtube.com/watch?v=aF552bMEcO4
  """

drivers = {
    'MS_ACCESS': 'Microsoft Access Driver (*.mdb, *.accdb)',
            'MS_SQL': 'SQL Server',
            'MY_SQL': 'MySQL ODBC 3.51 Driver',
            'ORACLE': 'Oracle in OraClient11g_home1',
            'MARIADB': 'MariaDB Connector/C 3.1',
            'POSTGRESQL': 'PostgreSQL Unicode'
}

conn = None

def __init__(self, driver, server, database, trusted='yes'):
  self.driver = '{' + driver + '}'
  self.server = server
  self.database = database
  self.trusted = trusted
  try:
    pyodbc.connect(
        "Driver={};Server={};Database={};Trusted_Connection={}".format(self.driver, self.server, self.database, self.trusted
                                                                        ))
  except pyodbc.Error as e:
    sqlstate = e.args[1]
    logger.warning(sqlstate)
  else:
    querying.conn = pyodbc.connect(
        "Driver={};Server={};Database={};Trusted_Connection={}".format(self.driver, self.server, self.database, self.trusted))
  
def create(self, sql):
  try:
    pass
  except pyodbc.Error as e:
    sqlstate = e.args[1]
    logger.warning(sqlstate)
  else:
    querying.conn.commit()
  finally:
    pass

def read(self, sql):
  # using self to provide the connection string it executes a query based on the SQL provided and returns a dataframe
  try:
    cursor = querying.conn.cursor()
  except pyodbc.Error as e:
    sqlstate = e.args[1]
    logger.warning(sqlstate)
  else:
    return pd.read_sql(sql, cursor)
  finally:
    pass


def update(self, sql):
  try:
    pass
  except pyodbc.Error as e:
    sqlstate = e.args[1]
    logger.warning(sqlstate)
  else:
    querying.conn.commit()
  finally:
    pass

def delete(self, sql):
  try:
    pass
  except pyodbc.Error as e:
    sqlstate = e.args[1]
    logger.warning(sqlstate)
  else:
    querying.conn.commit()
  finally:
    pass