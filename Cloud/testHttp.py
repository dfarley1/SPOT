import requests
import pprint
import pickle

#base_url = 'http://127.0.0.1:8000/sensor/'
base_url = 'http://alien-walker-157903.appspot.com/sensor/'
get_args = {'sensor_id': '1234'}
#get_args="/sensor/?sensor_id=1234"
post_args="occ_status=1&occ_since=2017-02-20%2013:34:00&occ_license=4AME671"
cookie_filename = '/home/pi/spot_log/py_cookies.txt'

def testGET():
    r = requests.get(base_url, params = get_args)
    print(r.cookies['csrftoken'])
    saveCookies(r.cookies)
    printResponse(r)


def testPOST():
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
            'occ_status': '1',
            'occ_since': '2017-02-20%2013:34:00',
            'occ_license': '4AME671',
            'csrfmiddlewaretoken': cookies['csrftoken']
        },
        cookies = cookies
    )
    
    printResponse(r)


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
