import requests
import pprint
import pickle
import uuid
import os
import datetime

base_url = 'http://127.0.0.1:8000/'
cookie_file = os.getcwd()+"/../py_cookies.txt"

def sensor_GET():
	cookies = loadCookies()
	params = {'sensor_uuid': cookies['sensor_uuid']}
	
	r = requests.get(base_url+"sensor/", params=params)
	
	saveCookies(r.cookies)
	printResponse(r)


def sensor_POST():
	cookies = loadCookies()
	params = {'sensor_uuid': cookies['sensor_uuid']}
	data = {
		'occ_status': '9876',
		'occ_since': datetime.datetime.now(),
		'occ_license': 'HelloWorld',
		'csrfmiddlewaretoken': cookies['csrftoken'],
	}
	
	r = requests.post(
		base_url+"sensor/",
		params = params,
		data = data,
		cookies = cookies,
	)
	
	printResponse(r)

def sensor_getUUID_GET():
	params = {'mac_addr': uuid.getnode()}
	r = requests.get(base_url+'sensor/getUUID/', params = params)
	print(r.cookies['csrftoken'])
	saveCookies(r.cookies)
	printResponse(r)










def saveCookies(requests_cookiejar):
	with open(cookie_file, 'wb') as f:
		pickle.dump(requests_cookiejar, f)


def loadCookies():
	with open(cookie_file, 'rb') as f:
		return pickle.load(f)


def printResponse(r):
	print("------ GET: Status = " + str(r.status_code) + " -----")
	print('----------- Headers ----------')
	for key,val in r.headers.items():
		print key, " : ", val
	print('------------ Text ------------')
	print(r.text)
	print('------------------------------\n\n')
