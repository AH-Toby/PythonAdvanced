# -*- coding:utf-8 -*-
import time


def application(environ, start_response):
    """wsgi"""
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    return str(environ) + '==Hello world from a simple WSGI application!--->%s\n' % time.ctime()
