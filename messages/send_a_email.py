from .email import emails

message = emails('kino.mondesir@gmail.com', 'Nik0l@$')
message.receivers('morel.kevin@gmail.com')
message.send()