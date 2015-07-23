#!/usr/bin/env python

from app import app

if '__main__' == __name__:
    app.run('0.0.0.0', port=8585)
