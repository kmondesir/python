


from contextlib import contextmanager
import sys
import os
import datetime as dt

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

file_handler = log.FileHandler(os.path.splitext(__file__)[0] + "." + "log")
file_handler.setLevel(severity["INFO"])
file_handler.setFormatter(formatter)

stream_handler = log.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

class items:

  """
  Opens a file for reading, writing and updating

  The code references a video 'Python Tutorial: Context Managers - Efficiently Managing Resources' 
  created by Corey Schafer and is part of a video series

  https://www.youtube.com/redirect?redir_token=tKiuOsI1ZF8oNIDLKASs2PhnbWZ8MTU3MDk5ODI1M0AxNTcwOTExODUz&q=https%3A%2F%2Fgithub.com%2FCoreyMSchafer%2Fcode_snippets%2Ftree%2Fmaster%2FPython-Context-Managers&v=-aKFBoZpiqA&event=video_description
  
  https://www.daniweb.com/programming/software-development/threads/191670/saving-to-creating-a-new-folder 
  """

  def __init__(self, path=os.getcwd()):
    # tests whether the file exists and throws an error if not
    self.path = path
    try:
      os.path.exists(self.path)
	except PermissionError as e:
      logger.warning(e)
	except FileNotFoundError as e:
      logger.warning(e)
    except OSError as e:
      logger.warning(e)
    except Exception as e:
      logger.warning(e)
    else:
      # changes the current directory
      os.chdir(self.path)


  def read(self, item):
    # open a file and returns its contents to the caller
    self.item = item
    try:
      f = open(self.item, 'r+')
    except PermissionError as e:
      logger.warning(e)
    except FileNotFoundError as e:
      logger.warning(e)
    except OSError as e:
      logger.warning(e)
    except Exception as e:
      logger.warning(e)
    else:
      return f


  def write(self, value, item=(dt.datetime.now().strftime("D%m-%d-%YT%H:%M:%S")) + "." + "tmp"):
    # opens a file and writes to it
    
    if os.path.exists(item):
      print("File already exist, please use the append method")
      raise FileExistsError
    else:
      self.item = item
    
    try:
      f = open(self.item, 'w+')
    except PermissionError as e:
      logger.warning(e)
	except FileExistsError as e:
		logger.warning(e)
    except OSError as e:
      logger.warning(e)
    except Exception as e:
      logger.warning(e)
    else:
      f.write(value)
    finally:
      f.close()


  def append(self, item, value="This line was generated at" + " " + dt.datetime.now().strftime("D%m-%d-%YT%H:%M:%S") + "\n"):
    # opens a file and appends data to it
    self.item = item
    try:
      f = open(self.item, 'a+')
    except PermissionError as e:
      logger.warning(e)
	except FileNotFoundError as e:
      logger.warning(e)
    except OSError as e:
      logger.warning(e)
    except Exception as e:
      logger.warning(e)
    else:
      f.write(value)
    finally:
      f.close()
