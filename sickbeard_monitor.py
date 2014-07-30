# This code will be the bits that monitor sickbeard.

from urllib2 import urlopen, URLError, HTTPError
import json
from gpiocrust import Header, OutputPin

def call_sb(sb_api_key, sb_ip, sb_port, sb_api):
    try:
        response = urlopen('http://{}:{}/api/{}/{}'.format(sb_ip, sb_port, sb_api_key, sb_api ))
        return response

    except HTTPError, e:
        return e.code

    except URLError, e:
        return e.reason


if __name__ == '__main__':

    sb_api_key = 'e4bf3dc3c82dd28fab47c83dcb3a2f16'
    sb_ip = '172.16.140.140'
    sb_port = '8081'
    sb_api = 'sb.ping'

    response = call_sb(sb_api_key, sb_ip, sb_port, sb_api)

    try:
        response2 = json.load(response)

    except:
        response2 = {'result': 'broke'}

    test = response2['result']

    if test == 'success':
        print 'Sickbeard is up'
        with Header() as header:
            pin = OutputPin(22, value=1)
    else:
        print 'Sickbeard is down'
        with Header() as header:
            pin = OutputPin(22, value=0)



