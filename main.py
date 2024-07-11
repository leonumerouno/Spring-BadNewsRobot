import requests
import json
import os

session = requests.Session()
cookies = {'token': os.environ['TOKEN']}
session.cookies.update(cookies)

# 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJFeHBpcmVBdCI6MTcyMDc2ODk3OCwiVW5pb25JRCI6Im9Jalp4NlV5akZFRnQ0cVlpcjhnbFdXdEs4M1UifQ.JRg_W3Wh__WFODSXIRhoHzomZF7n5nEtDU_rZaK61JU'
# url = "https://swjtu-grade-push.tpam.top/notions"

response = session.get(os.environ['GETURL'])

resp = json.loads(response.text)

posturl = "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=chat_id"

headers = {'Authorization': os.environ['HEADERS']}

# Bearer t-g1047bfxUYK4E7BAEV73D2P4A5WBFNWLVQ367CPL

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



