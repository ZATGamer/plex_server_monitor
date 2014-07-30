# This code will be the bits that monitor sickbeard.

from urllib2 import urlopen, URLError, HTTPError
import json
from gpiocrust import Header, OutputPin
import time
import socket
import datetime


def call_sb(sb_api_key, sb_ip, sb_port, sb_api):
    try:
        socket.setdefaulttimeout(5)
        response = urlopen('http://{}:{}/api/{}/{}'.format(sb_ip, sb_port, sb_api_key, sb_api ))
        return response, True

    except HTTPError, e:
        return e.code, False

    except URLError, e:
        return e.reason, False


if __name__ == '__main__':
    last_run = datetime.datetime.now() - datetime.timedelta(seconds=10)
    sb_api_key = 'd1adef047c3d9c52bf65bfe709831b18'
    sb_ip = '10.180.181.120'
    sb_port = '8081'
    sb_api = 'sb.ping'
    up = bool
    fails = 0

    while True:

        if last_run + datetime.timedelta(seconds=10) <= datetime.datetime.now():
            last_run = datetime.datetime.now()

            response, up = call_sb(sb_api_key, sb_ip, sb_port, sb_api)

            if up is True:
                response2 = json.load(response)
                test = response2['result']

                if test == 'success':
                    fails = 0
                    print 'Sickbeard is up'
                    with Header() as header:
                        pin = OutputPin(22, value=1)
                else:
                    fails += 1
                    if fails < 1:
                        print 'Sickbeard is WARNING'
                    elif fails >= 1:
                        print 'Sickbeard is DOWN'
                        with Header() as header:
                            pin = OutputPin(22, value=0)
            else:
                if fails < 1:
                    print fails
                    fails += 1
                    print 'Sickbeard is WARNING didn\'t return expected json'
                elif fails >= 1:
                    print fails
                    fails += 1
                    print 'Sickbeard didn\'t return expected json'
                    with Header() as header:
                        pin = OutputPin(22, value=0)
