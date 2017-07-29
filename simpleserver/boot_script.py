import http.server
import os
import socketserver
import sys


# invoke point gonna be python's work space
dir = os.path.dirname(os.path.abspath(__file__))
print ("Python work in the dir [" + dir +"]")
os.chdir(dir)

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("",PORT),Handler)
print("serving at port",PORT)
httpd.serve_forever()
