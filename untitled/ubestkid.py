import requests
import os
import json

os.makedirs('./ani/', exist_ok=True)
def download():
    response = requests.get("http://service2.ubestkid.com:8081/1/getvideos.json?subcateid=65&p=1&ps=80")
    # print(type(response))
    json_response = response.content.decode()
    print(type(json_response))
    dict_json = json.loads(json_response)
    print(type(dict_json['items']))

    items = dict_json['items']


    for obj in items:
        print(obj['url'])
        r = requests.get(obj["url"], stream=True)
        with open('./ani/' + obj['title'] + '.mp4', 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)

if __name__ == '__main__':

    download()