


import sys
import os
import datetime as dt
import smtplib, ssl, email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create a secure SSL context
context = ssl.create_default_context()

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

class send_email:

  """
  Opens a file for reading, writing and updating

  The code references a video 'Python Tutorial: Context Managers - Efficiently Managing Resources' 
  created by Corey Schafer and is part of a video series

  https://www.youtube.com/redirect?redir_token=tKiuOsI1ZF8oNIDLKASs2PhnbWZ8MTU3MDk5ODI1M0AxNTcwOTExODUz&q=https%3A%2F%2Fgithub.com%2FCoreyMSchafer%2Fcode_snippets%2Ftree%2Fmaster%2FPython-Context-Managers&v=-aKFBoZpiqA&event=video_description
  
  https://www.daniweb.com/programming/software-development/threads/191670/saving-to-creating-a-new-folder 
  """

  def __init__(self, sender, receiver, server='smtp.gmail.com', port=587):
    # https://realpython.com/python-send-email/
    self.sender = sender
    self.receiver = receiver
    self.server = server
    self.port = port
    
    
    try:
      context = ssl.create_default_context() 
      server = smtplib.SMTP(self.server,self.port)
      server.starttls(context=context)
      
    except Exception as e:
      logger.error(e)
    else:
      pass

  def send(self, subject='Default message sent at {}'.format(dt.datetime.now()), message=None):
    self.subject = subject
    self.message = message

    msg = MIMEMultipart("alternative")
    msg["Subject"] = self.subject
    msg["From"] = self.sender
    msg["To"] = self.receiver

    try:
      pass
    except Exception as e:
      logger.error(e)
    else:
      # Create secure connection with server and send email
      context = ssl.create_default_context()
    finally:
      pass
