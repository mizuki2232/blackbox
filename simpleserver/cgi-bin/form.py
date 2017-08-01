#!/usr/bin/env python
import cgi


print "Content-Type: text/html\n"
print "<html><body>"


form = cgi.FieldStorage()


class MyHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):           
        self.send_response(200, "ok")       
        self.send_header('Access-Control-Allow-Origin', '*')                
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")        

    def do_GET(self):           
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type',    'text/html')                                    
        self.end_headers()              
        self.wfile.write("<html><body>Hello world!</body></html>")
        self.connection.shutdown(1) 


if form.has_key("object"):
    print(form["name"].value)
    MyHandler.do_OPTIONS()
    MyHandler.do_GET()


print "<body></html>"
