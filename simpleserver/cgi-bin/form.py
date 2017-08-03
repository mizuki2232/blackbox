#!/usr/bin/env python
import cgi
import cgitb
import json


# show error detail in client
cgitb.enable()

# load json
config_json = open('json/config.json', 'r')
config = json.load(config_json)


print("Content-Type: text/html\n")
print("")
print("<html><body>")


form = cgi.FieldStorage()


if form.has_key("object"):
    print("<h1>What I'll watch is</h1><br>")
    print(form["object"].value)
    print("</body></html>")

else:
    print("The Post request doesn't contain object")


for attr in config.get("list"):
    if attr.get("id") == "Watch_Object":
        print(attr.get('body'))

print("</body></html>")
