import requests
import json
import os

session = requests.Session()
cookies = {'token': os.environ['TOKEN']}
session.cookies.update(cookies)

response = session.get(os.environ['GETURL'])

resp = json.loads(response.text)

posturl = "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=chat_id"

headers = {'Authorization': os.environ['HEADERS']}

if resp['msg'] == "ok":
    datas = {
        "receive_id": os.environ['RECEIVEID'],
        "content": "{\"text\":\"server running\"}",
        "msg_type": "text"
    }
    response = session.post(url=posturl,data=datas,headers = headers)
    print(response.text)

else:
    datas = {
        "receive_id": os.environ['RECEIVEID'],
        "content": "{\"text\":\"server G\"}",
        "msg_type": "text"
    }
    response = session.post(url=posturl, data=datas, headers=headers)
    print(response.text)



