


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
formatter = log.Formatter('timestamp:%(asctime)s module:%(name)s message:%(message)s')

filename = os.path.splitext(__file__)[0]
extension = "log"
file_handler = log.FileHandler(filename + "." + extension)
file_handler.setLevel(severity['INFO'])
file_handler.setFormatter(formatter)

stream_handler = log.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

class connections:

  """
  Creates a connection string 

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

  def __init__(self, driver=drivers['MS_SQL'], server='127.0.0.1', trusted='yes'):
    self.driver = '{' & driver & '}'
    self.server = server
    self.trusted = trusted
    try:
      self.connect = pyodbc.connect("Driver={};Server={};Trusted_Connection={}".format(self.driver, self.server, self.trusted))
    except pyodbc.Error as e:
      sqlstate = e.args[1]
      logger.warning(sqlstate)
    else:
      result = self.connect
  
  def __repr__(self):
    pass
  
  def __str__(self):
    pass
    
class manipulations(connections):
  
  def __init__(self, driver, server, trusted, database, user, password):
    # https://www.youtube.com/watch?v=RSl87lqOXDE&t=100s 
    super().__init__(driver, server, trusted)
    self.database = "Database={}".format(database)
    self.user = "UID={}".format(user)
    self.password = "PWD={}".format(password)
    self.connect += ";".join(self.database,';',self.user,';',self.password)
    
  def insert(self, sql):
    try:
      cursor = self.connect.cursor()
      cursor.execute(sql)
    except pyodbc.Error as e:
      sqlstate = e.args[1]
      logger.warning(sqlstate)
    else:
      self.connect.commit()
    finally:
      cursor = None
      self.connect = None

  def update(self, sql):
    try:
      cursor = self.connect.cursor()
      cursor.execute(sql)
    except pyodbc.Error as e:
      sqlstate = e.args[1]
      logger.warning(sqlstate)
    else:
      self.connect.commit()
    finally:
      self.connect = None
      cursor = None

  def delete(self, sql):
    try:
      cursor = self.connect.cursor()
      cursor.execute(sql)
    except pyodbc.Error as e:
      sqlstate = e.args[1]
      logger.warning(sqlstate)
    else:
      self.connect.commit()
    finally:
      self.connect = None
      cursor = None
    
  def merge(self, sql):
    pass
  
  def call(self, sql):
    pass
   
  class definitions(connections):

    def __init__(self, driver, server, trusted, database, user, password):
      super().__init__(driver, server, trusted)
      self.database = "Database={}".format(database)
      self.user = "UID={}".format(user)
      self.password = "PWD={}".format(password)
      self.connect += ";".join(self.database,';',self.user,';',self.password)
    
    def create(self, sql):
      pass
    
    def alter(self, sql):
      pass
    
    def drop(self, sql):
      pass
    
    def rename(self, sql):
      pass
    
    def tuncate(self, sql):
      pass
    
    def comment(self, sql):
      pass
    
  class queries(connections):
    
    def __init__(self, driver, server, trusted, database, user, password):
      super().__init__(driver, server, trusted)
      self.database = "Database={}".format(database)
      self.user = "UID={}".format(user)
      self.password = "PWD={}".format(password)
      self.connect += ";".join(self.database,';',self.user,';',self.password)
    
    def select(self, sql):
      try:
        cursor = self.connect.cursor()
        cursor.execute(sql)
      except pyodbc.Error as e:
        sqlstate = e.args[1]
        logger.warning(sqlstate)
      else:
        rows = list(cursor.fetchall())
        return rows