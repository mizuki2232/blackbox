#!/usr/bin/env python
import cgi
import cgitb


# show error detail in client
cgitb.enable()


print("Content-Type: text/html\n")
print("")
print("<html><body>")


form = cgi.FieldStorage()


if form.has_key("object"):
    print("<h1>What I'll watch is</h1><br>")
    print(form["object"].value)
    print("<body></html>")

else:
    print("The Post request doesn't contain object")
    print("<html><body>")
