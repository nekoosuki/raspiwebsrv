import requests

url1='http://localhost/cgi-bin/config.py'

url2='http://localhost/cgi-bin/fupld.py'

file='../json/config.json'

requests.post(url1,data={'conf':0.5,'iou':0.5,'state':0,'sql':0})

requests.post(url2,files={'file':open(file,encoding='utf-8')})


