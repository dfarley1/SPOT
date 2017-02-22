import requests

url = 'http://alien-walker-157903.appspot.com/sensor/'
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url)
print(r.text)
r1 = requests.post(url, data=payload)
print(r1.text)