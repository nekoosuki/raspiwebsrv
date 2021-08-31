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
            j = json.load(f)
            ip = j['srv_ip']
            port = j['srv_port']
            id = j['dev_id']
        conn = pymysql.Connect(host=ip,port=port,user='root',passwd='yang2000yuzhe',db='raspi')
        cur = conn.cursor()
        cur.execute(f'update config set conf={conf}, iou={iou} where dev_id="{id}";')
    except:
        # 提交数据库失败
        conn.rollback()
        syn = -1
    else:
        # 提交数据库成功
        syn = 1
    finally:
        cur.close()
else:
    # 未提交数据库
    syn = 0

data.update({'syn':syn})

try:
    with open('json/config.json', 'w') as f:
            json.dump(data, f, indent=4)
except:
    # 提交本地失败
    local = -1
    if syn == 1:
        conn.rollback()
else:
    # 提交本地成功
    local = 1
finally:
    #关闭游标和连接
    if syn != 0:
        conn.commit()
        conn.close()

data.update({'local':local})

print("Content-type: application/json\n")
print(json.dumps(data))
