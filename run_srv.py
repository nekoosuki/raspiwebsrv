#!C:\Users\DELL_USER\anaconda3\envs\py38\python.exe
# -*- coding: UTF-8 -*-

from http.server import HTTPServer, CGIHTTPRequestHandler
import argparse

parser = argparse.ArgumentParser('python run_srv.py')
parser.add_argument('-p', '--port', type=int, default=80, help='port which server is running on')
args = parser.parse_args()
httpd = HTTPServer(('', args.port), CGIHTTPRequestHandler)
print(f'starting httpd on port {args.port}')
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('shutting down')
    httpd.shutdown()