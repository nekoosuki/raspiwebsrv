# -*- coding: UTF-8 -*-

import cgi
import json
import pymysql

form = cgi.FieldStorage()
conf = eval(form.getvalue("conf"))
iou = eval(form.getvalue("iou"))
state = eval(form.getvalue("state"))
sql = eval(form.getvalue("sql"))

if sql:
    with open('json/dev_info.json', 'r') as f:
        ip = json.load(f)['srv_ip']
    # TODO 提交数据库
data = {"conf": conf, "iou": iou, "state": state}
with open('json/config.json', 'w') as f:
    json.dump(data, f, indent=4)
print("Content-type: application/json\n")
print(json.dumps(data))
