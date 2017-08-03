from http.server import HTTPServer, CGIHTTPRequestHandler, SimpleHTTPRequestHandler
import os
import socketserver
import sys


# invoke point gonna be python's work space
dir = os.path.dirname(os.path.abspath(__file__))
print ("Python Server Launch in the dir [" + dir +"]")
os.chdir(dir)

PORT = 8000


class CGIHandler(CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]


httpd = HTTPServer(("",PORT),CGIHandler)
print("serving at port",PORT)
httpd.serve_forever()
