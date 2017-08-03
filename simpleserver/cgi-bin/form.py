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
    print("<h1>What I'll watch is</h1><br><hr>")
    for attr in config.get("list"):
        if attr.get("id") == "Watch_Object":
            attr["body"] = form["object"].value
            print("<h1>")
            print(attr.get('body'))
            print("</h1>")


else:
    print("<h1>" + "The Post request doesn't contain object" + "</h1>")



# write config.json
config_json = open('json/config.json', 'w')
json.dump(config, config_json, indent=4, sort_keys=True, separators=(',', ': '))


print("</body></html>")
