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

class opening:
  
  """
  Opens a file for reading from or writing to

  The code references a video 'Python Tutorial: Context Managers - Efficiently Managing Resources' 
  created by Corey Schafer and is part of a video series

  https://www.youtube.com/redirect?redir_token=tKiuOsI1ZF8oNIDLKASs2PhnbWZ8MTU3MDk5ODI1M0AxNTcwOTExODUz&q=https%3A%2F%2Fgithub.com%2FCoreyMSchafer%2Fcode_snippets%2Ftree%2Fmaster%2FPython-Context-Managers&v=-aKFBoZpiqA&event=video_description
  """

  fullpath = None

  def __init__(self, path=os.getcwd(), item=os.__file__):
    # tests whether the file exists and throws an error if not
    self.path = path
    self.item = item
    opening.fullpath = os.path.join(path, item)
    try:
      os.path.exists(opening.fullpath)
    except IOError as e:
      logger.warning(e)
    except Exception as e:
      logger.warning(e)
    
  def read(self):
    # open a file and returns its contents to the caller
    try:
      f = open(opening.fullpath, 'r')
    except PermissionError as e:
      logger.warning(e)
    except IOError as e:
      logger.warning(e)
    except Exception as e:
      logger.warning(e)
    else: 
      return f
    finally:
      f.close()

  def write(self, value):
    # opens a file and writes to it
    try:
      f = open(opening.fullpath, 'w')
    except PermissionError as e:
      logger.warning(e)
    except IOError as e:
      logger.warning(e)
    except Exception as e:
      logger.warning(e)
    else:
      f.write(value)
    finally:
      f.close()

class querying:

  """
  Creates a connection string and provides CRUD methods for data manipulation

  This video demostrates how to connect to SQL with Python using the pyodbc class, 
  this may not be the best way to connect but its the simplest to understand

  https://www.youtube.com/watch?v=aF552bMEcO4
  """

drivers = {
            'MS_ACCESS': 50,
            'MS_SQL': 40,
            'MY_SQL': 30,
            'ORACLE': 20,
            'MARIADB': '',
            'POSTGRESQL': ''
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
