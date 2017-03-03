import requests
import pprint
import pickle
import uuid
import os

base_url = 'http://127.0.0.1:8000/'
#base_url = 'http://alien-walker-157903.appspot.com/sensor/'
get_args = {'sensor_uuid': '00000000-0000-0000-0000-000000000001'}
#get_args="/sensor/?sensor_id=1234"
post_args="occ_status=1&occ_since=2017-02-20%2013:34:00&occ_license=4AME671"
#cookie_filename = '/home/pi/spot_log/py_cookies.txt'
cookie_filename = 'django/py_cookies.txt'

def sensor_GET():
	cookies = loadCookies()
	params = {'sensor_uuid': cookies['sensor_uuid']}
	
	r = requests.get(base_url+"sensor/", params=params)
	
	saveCookies(r.cookies)
	printResponse(r)


def sensor_POST():
	cookies = loadCookies()
	print(cookies['csrftoken'])
	
	print('----------')
	for key, val in cookies.items():
		print key, " : ", val
	print('----------')
	
	r = requests.post(
		base_url,
		params = get_args,
		data = {
			#'occ_status': occupied_status,
			'occ_status': '1',
			# 'occ_since': occupied_since,
			'occ_since': '2017-02-20%2013:34:00',
			# 'occ_license': occupied_license,
			'occ_license': '4AME671',
			'csrfmiddlewaretoken': cookies['csrftoken']
		},
		cookies = cookies
	)
	printResponse(r)

def sensor_getUUID_GET():
	params = {'mac_addr': uuid.getnode()}
	r = requests.get(base_url+'sensor/getUUID/', params = params)
	print(r.cookies['csrftoken'])
	saveCookies(r.cookies)
	printResponse(r)










def saveCookies(requests_cookiejar):
	with open(os.getcwd()+"/../py_cookies.txt", 'wb') as f:
		pickle.dump(requests_cookiejar, f)


def loadCookies():
	with open(os.getcwd()+"/../py_cookies.txt", 'rb') as f:
		return pickle.load(f)


def printResponse(r):
	print("------ GET: Status = " + str(r.status_code) + " -----")
	print('----------- Headers ----------')
	for key,val in r.headers.items():
		print key, " : ", val
	print('------------ Text ------------')
	print(r.text)
	print('------------------------------\n\n')
