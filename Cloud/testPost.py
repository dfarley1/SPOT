import requests

url = 'http://alien-walker-157903.appspot.com/sensor/'
r = requests.get(url)
print r.status_code
print r.content
print r.encoding
r.text
print r.text

