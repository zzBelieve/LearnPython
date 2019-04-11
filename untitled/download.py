import requests

import json
import os
os.makedirs('./sound/', exist_ok=True)

f = open("ani.json", encoding='utf-8')
aa = json.load(f)

for ani in aa:
    # print(ani["pic"])
    # r = requests.get(ani["pic"], stream=True)
    # with open('./image/'+ani['name'] + '.png', 'wb') as f:
    #     for chunk in r.iter_content(chunk_size=32):
    #         f.write(chunk)

    print(ani["sound"])
    r = requests.get(ani["sound"], stream=True)
    with open('./sound/'+ani['name'] + '.mp3', 'wb') as f:
      for chunk in r.iter_content(chunk_size=32):
          f.write(chunk)

f.close()