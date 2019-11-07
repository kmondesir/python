from email import mail



message = mail('kino.mondesir@gmail.com')
message.receivers('morel.kevin@gmail.com')
message.send()