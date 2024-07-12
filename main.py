import requests
import json
import os

#获取tenant_access_token
token_url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"

datas = {
    "app_id": os.environ['APPID'],
    "app_secret": os.environ['APPSECRET']
}

resp = requests.post(token_url,data=datas)
auth = "Bearer " + json.loads(resp.text)['tenant_access_token']

#访问喷泉
session = requests.Session()
cookies = {'token': os.environ['TOKEN']}
session.cookies.update(cookies)

try:
    response = session.get(os.environ['GETURL'],timeout=10)
except requests.exceptions.RequestException as e:
    #如果超时，飞书机器人发消息
    posturl = "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=chat_id"
    headers = {'Authorization': auth}
    datas = {
            "receive_id": os.environ['RECEIVEID'],
            "content": "{\"text\":\"<at user_id=\\\\\"" + os.environ['USERID'] + "\\\">马熙翔</at> 服务器停止运行\"}",
            "msg_type": "text"
        }
    response = session.post(url=posturl, data=datas, headers=headers)
    print(response.text)


