


from contextlib import contextmanager
import sys
import os

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

file_handler = log.FileHandler('files.log')
file_handler.setLevel(severity["INFO"])
file_handler.setFormatter(formatter)

stream_handler = log.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

class items:

  """
  Opens a file for reading from or writing to

  The code references a video 'Python Tutorial: Context Managers - Efficiently Managing Resources' 
  created by Corey Schafer and is part of a video series

  https://www.youtube.com/redirect?redir_token=tKiuOsI1ZF8oNIDLKASs2PhnbWZ8MTU3MDk5ODI1M0AxNTcwOTExODUz&q=https%3A%2F%2Fgithub.com%2FCoreyMSchafer%2Fcode_snippets%2Ftree%2Fmaster%2FPython-Context-Managers&v=-aKFBoZpiqA&event=video_description
  """

  def __init__(self, path=os.getcwd()):
    # tests whether the file exists and throws an error if not
    self.path = path
    try:
      os.path.exists(self.path)
    except IOError as e:
      logger.warning(e)
    except Exception as e:
      logger.warning(e)


  def read(self, item):
    # open a file and returns its contents to the caller
    self.item = item
    self.fullpath = os.path.join(self.path, self.item)
    try:
      f = open(self.fullpath, 'r+')
    except PermissionError as e:
      logger.warning(e)
    except IOError as e:
      logger.warning(e)
    except Exception as e:
      logger.warning(e)
    else:
      return f


  def write(self, value, item):
    # opens a file and writes to it
    self.item = item
    self.fullpath = os.path.join(self.path, self.item)
    try:
      f = open(self.fullpath, 'w+')
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


  def append(self, value, item):
    # opens a file and appends data to it
    self.item = item
    self.fullpath = os.path.join(self.path, self.item)
    try:
      f = open(self.fullpath, 'a+')
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