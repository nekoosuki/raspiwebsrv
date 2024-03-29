import pymysql
import json

with open('json/dev_info.json', 'r') as f:
    j = json.load(f)
    ip = j['srv_ip']
    port = j['srv_port']
    id = j['dev_id']

conn = pymysql.Connect(host=ip, port=port,user='root',passwd='yang2000yuzhe',db='raspi')
cur = conn.cursor()
cur.execute(f'select conf,iou from config where dev_id="{id}";')

result = cur.fetchall()[0]
conf = result[0]
iou = result[1]

cur.close()
conn.close()

print("Content-type: application/json\n")
print(json.dumps({'conf':conf,'iou':iou}))