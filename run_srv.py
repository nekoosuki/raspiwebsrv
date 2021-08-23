#!C:\Users\DELL_USER\anaconda3\envs\py38\python.exe
# -*- coding: UTF-8 -*-

from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8081
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print(f'starting httpd on port {port}')
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('shutting down')
    httpd.shutdown()