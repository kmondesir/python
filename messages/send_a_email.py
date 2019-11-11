from message import emails


message = emails('kino.mondesir@gmail.com')
message.senders('kino.mondesir@gmail.com')
message.receivers('morel.kevin@gmail.com')
message.send()
