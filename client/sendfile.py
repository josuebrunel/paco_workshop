#!/usr/bin/env python

##################################################
#
#   Author          : josuebrunel
#   Filename        : sendfile.py
#   Description     :
#   Creation Date   : 21-07-2015
#   Last Modified   : Sun Jul 26 18:15:05 2015
#
##################################################

import sys
import pdb
import requests

def send_file(filename, filetype):
    url = 'http://212.83.154.157:8585/upload_file'
    files = {'filename': (filename, open(filename, 'rb'), 'application/{0}'.format(filetype), {'Expires': '0'})}
    #files = {'filename': (filename, open(filename, 'rb'), 'application/x-gzip', {'Expires': '0'})}

    response = requests.post(url, files=files, allow_redirects= True)

    print(response.status_code)


if '__main__' == __name__ :
    filename = sys.argv[1]
    filetype = sys.argv[2]

    send_file(filename, filetype)
