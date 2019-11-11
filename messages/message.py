


import sys
import os
import datetime as dt
import smtplib, ssl, email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from getpass import getpass

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

filename = os.path.splitext(__file__)[0]
extension = "log"
file_handler = log.FileHandler(filename + "." + extension)
file_handler.setLevel(severity["INFO"])
file_handler.setFormatter(formatter)

stream_handler = log.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

class emails:

  """
  Creates a email 

    your_message.receivers('receipient')
    your_message.message('The subject','and Body')
    your_message.send

  The syntax is broken into multiple parts making it more verbose but easier to read

  """

  def __init__(self, username, server='smtp.gmail.com', port=587):
    # https://realpython.com/python-send-email/
    self.username = username
    # https://stackoverflow.com/questions/9202224/getting-command-line-password-input-in-python
    self.password = getpass()
    self.server = server
    self.port = port
    
    try:
      self.mail = smtplib.SMTP(server, port)
    except Exception as e:
      logger.error(e)
    else:
      self.mail.login(self.username, self.password)

  def senders(self, sender=None):
    # Adds from field to the object
    if sender is None:
      self.sender = self.username
    else:
      self.sender = sender

  def receivers(self, receiver, carbon_copy=None, blind_carbon_copy=None):
    # Adds a to, cc, and bcc attributes to the email object   
    self.receiver = receiver   
    self.carbon_copy = carbon_copy
    self.blind_carbon_copy = blind_carbon_copy
    
  def message(self, subject='Default message sent at {}'.format(dt.datetime.now()), body=None):
    # Add subject and body to the email object
    self.subject = subject
    self.body = body

  def send(self, files=None):
    # Send the email object once sender, receivers and message have been executed
    try:
      self.files = files
      msg = MIMEMultipart("alternative")
      
      if self.carbon_copy is not None:
        msg["Cc"] = self.carbon_copy
        
      if self.blind_carbon_copy is not None:
        msg["Bcc"] = self.blind_carbon_copy

      # sets up message variables
      msg["To"] = self.receiver
      msg["From"] = self.sender
      msg["Subject"] = self.subject
      
      # add in the message body
      msg.attach(MIMEText(self.body, 'plain'))
    except Exception as e:
      logger.error(e)
    else:
      self.mail.send_message(msg, self.senders)
    finally:
      self.mail.quit()