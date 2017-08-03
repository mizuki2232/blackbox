from http.server import HTTPServer, CGIHTTPRequestHandler, SimpleHTTPRequestHandler
import os
import socketserver
import sys


# invoke point gonna be python's work space
dir = os.path.dirname(os.path.abspath(__file__))
print ("Python Server Launch in the dir [" + dir +"]")
os.chdir(dir)

PORT = 8000


class MyHandler(SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With')

    def do_POST(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.connection.shutdown(1)


class CGIHandler(CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]


httpd = HTTPServer(("",PORT),CGIHandler)
print("serving at port",PORT)
httpd.serve_forever()
