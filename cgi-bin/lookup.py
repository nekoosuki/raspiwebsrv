# -*- coding: UTF-8 -*-

import json

with open('json/config.json', 'r') as f:
    config = json.load(f)
with open('json/dev_info.json', 'r') as f:
    dev = json.load(f)

print("Content-type: application/json\n")
data = {**config, **dev}
print(json.dumps(data))
