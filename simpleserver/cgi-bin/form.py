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


print("<h1>What I'll watch is</h1><br><hr>")


if form.has_key("object"):
    for attr in config.get("list"):
        if attr.get("id") == "Watch_Object":
            attr["body"] = form["object"].value
            print("<h1>")
            print(attr.get('body'))
            print("</h1>")


else:
    print("<h1>" + "The Post request doesn't contain object" + "</h1>")



print("<br><br><h1>Desired Count</h1><br><hr>")


if form.has_key("Count"):
    for attr in config.get("list"):
        if attr.get("id") == "Desired_Count":
            attr["body"] = form["Count"].value
            print("<h1>")
            print(attr.get('body'))
            print("</h1>")


else:
    print("<h1>" + "The Post request doesn't contain Desired Count" + "</h1>")


print("<br><br><h1>Desired_Wait_Time</h1><br><hr>")


if form.has_key("Wait_Time"):
    for attr in config.get("list"):
        if attr.get("id") == "Desired_Wait_Time":
            attr["body"] = form["Wait_Time"].value
            print("<h1>")
            print(attr.get('body'))
            print("</h1>")


else:
    print("<h1>" + "The Post request doesn't contain Desired Wait Time" + "</h1>")


print("<br><br><h1>Mail Address</h1><br><hr>")


if form.has_key("Mail_Address"):
    for attr in config.get("list"):
        if attr.get("id") == "Desired_Mail_Address":
            attr["body"] = form["Mail_Address"].value
            print("<h1>")
            print(attr.get('body'))
            print("</h1>")


else:
    print("<h1>" + "The Post request doesn't contain Mail Address" + "</h1>")


# rewrite config.json
config_json = open('json/config.json', 'w')
json.dump(config, config_json, indent=4, sort_keys=True, separators=(',', ': '))


print("</body></html>")
