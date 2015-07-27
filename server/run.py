#!/usr/bin/env python
import pdb
import sys
from app import app

if '__main__' == __name__:

    try:
        host = str(sys.argv[1])
    except:
        host = '0.0.0.0'
    
    try:
        port = int(sys.argv[2])
    except:
        port = 8585

    app.run(host, port=port)
