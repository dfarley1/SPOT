import requests
import pprint
import pickle
import uuid
import os
import datetime

#base_url = 'http://127.0.0.1:8000/sensor/'
base_url = 'http://alien-walker-157903.appspot.com/sensor/'
get_args = {'sensor_id': '1234'}
get_uuid = {'getuuid'}
#get_args="/sensor/?sensor_id=1234"
post_args="occ_status=1&occ_since=2017-02-20%2013:34:00&occ_license=4AME671"
cookie_filename = '/home/pi/spot_log/py_cookies.txt'
#cookie_filename = 'py_cookies.txt'

def sensor_GET():
    cookies = loadCookies()
    params = {'sensor_uuid': cookies['sensor_uuid']}
    
    r = requests.get(base_url+"sensor/", params=params)
    
    saveCookies(r.cookies)
    printResponse(r)

def sensor_POST(occupied_status, occupied_since):
    cookies = loadCookies()
    params = {'sensor_uuid': cookies['sensor_uuid']}
    data = {
        'occ_status': occupied_status,
        # 'occ_status': '1',
        'occ_since': occupied_since,
        # 'occ_since': datetime.datetime.now(),
        # 'occ_license': occupied_license,
        'occ_license': '4AME671',
        'csrfmiddlewaretoken': cookies['csrftoken']
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

#######################COOKIE CODE#############################

def saveCookies(requests_cookiejar):
    with open(cookie_filename, 'wb') as f:
        pickle.dump(requests_cookiejar, f)


def loadCookies():
    with open(cookie_filename, 'rb') as f:
        return pickle.load(f)


def printResponse(r):
    print("------ GET: Status = " + str(r.status_code) + " -----")
    print('----------- Headers ----------')
    for key,val in r.headers.items():
        print key, " : ", val
    print('------------ Text ------------')
    print(r.text)
    print('------------------------------\n\n')
