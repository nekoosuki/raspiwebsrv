# -*- coding: UTF-8 -*-

import cgi
import json
import pymysql

form = cgi.FieldStorage()
conf = eval(form.getvalue("conf"))
iou = eval(form.getvalue("iou"))
state = eval(form.getvalue("state"))
sql = eval(form.getvalue("sql"))

data = {"conf": conf, "iou": iou, "state": state}
if sql:
    try:
        with open('json/dev_info.json', 'r') as f:
                ip = json.load(f)['srv_ip']
            # TODO 提交数据库
    except:
        # 提交数据库失败
        syn = -1
        # 回滚
    else:
        # 提交数据库成功
        syn = 1
else:
    # 未提交数据库
    syn = 0

try:
    with open('json/config.json', 'w') as f:
            json.dump(data, f, indent=4)
except:
    # 提交本地失败
    local = -1
    if syn == 1:
        # 回滚
        pass
else:
    # 提交本地成功
    local = 1
finally:
    #关闭游标和连接
    pass

data.update({'syn':syn, 'local':local})

print("Content-type: application/json\n")
print(json.dumps(data))
