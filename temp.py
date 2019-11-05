


import requests

payload = {'page':2, 'count':25}
payload1 = {'username':'corey', 'password':'testing'}
r =  requests.get('https://httpbin.org/get', params=payload)
d = requests.get('https://httpbin.org/post', data=payload1)
print(r.text)
print(r.status_code)
print(r.ok)
print(d.text)