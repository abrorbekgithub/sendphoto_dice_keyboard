import requests
import json
from pprint import pprint
import os

token=os.environ["DOGTOKEN"]

def getUpdate():
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    res=requests.get(url=url)
    data=res.json()
    update=data["result"]
    return update

def randomphoto():
    url=f'https://dog.ceo/api/breeds/image/random'
    res=requests.get(url)
    data=res.json()
    return data["message"]

def sendPhoto(ids):
    url=f'https://api.telegram.org/bot{token}/sendPhoto'
    photo=randomphoto()
    p={
        "chat_id":ids,
        "photo":photo,
        "caption":"this is dog"
    }
    res=requests.get(url,params=p)
    return res.json()

def reply_markup(ids):
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    p={
        "chat_id":ids,
        "text":"Random Dogs Photo",
        "reply_markup":{
            "keyboard":[ [{"text":"Random Dog"}] ],
            "resize_keyboard":True
        }
    }
    res=requests.post(url,json=p)
    return res.json()

length=len(getUpdate())
length_last=len(getUpdate())

ids=getUpdate()[-1]["message"]["chat"]["id"]
start=getUpdate()[-1]["message"]["text"]
reply_markup(ids)

while True:
    ids=getUpdate()[-1]["message"]["chat"]["id"]
    text=getUpdate()[-1]["message"]["text"]
    length_last=len(getUpdate())
       
    if length!=length_last:
        reply_markup(ids)
        sendPhoto(ids=ids)
        length=length_last