import http.server
import os
import socketserver
import sys


# invoke point gonna be python's work space
dir = os.path.dirname(os.path.abspath(__file__))
print ("Python Server Launch in the dir [" + dir +"]")
os.chdir(dir)

PORT = 8000

# Handler = http.server.SimpleHTTPRequestHandler

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With')

    def do_GET(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<html><body>Hello world!</body></html>')
        self.connection.shutdown(1)

httpd = socketserver.TCPServer(("",PORT),MyHandler)
print("serving at port",PORT)
httpd.serve_forever()
