import requests
import json
import os
from pprint import pprint

token=os.environ["DOGTOKEN"]    #1

def getUpdates():          #2
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    res=requests.get(url=url)
    update=res.json()["result"]
    return update

def last():          #2
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    res=requests.get(url=url)
    update=res.json()["result"]
    return update[-1]

def ids_text():       #3
    ids=last()["message"]["from"]["id"]
    text=last()["message"]["text"]
    return ids,text

def randomPhoto():        #4
    url=f'https://dog.ceo/api/breeds/image/random'
    res=requests.get(url)   
    img_url=res.json()["message"]
    return img_url

def reply_markup(ids):    #5
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    p={
        "chat_id":ids,
        "text":"Dogs",
        "reply_markup":{
            "keyboard":[[{"text":"random dog"}]],
            "resize_keyboard":True
        }
    }
    res=requests.post(url,json=p)
    return res.json()

def sendPhoto(ids):   #6
    url=f'https://api.telegram.org/bot{token}/sendPhoto'
    photo=randomPhoto()
    p={
        "chat_id":ids,
        "photo":photo,
    }
    res=requests.get(url,params=p)
    return res.json()

len_update=len(getUpdates())
last_len_update=len(getUpdates())

while True:
    last_len_update=len(getUpdates())
    ids,text=ids_text()

    if last_len_update!=len_update:
        if text=='/start':
            reply_markup(ids)
            len_update=last_len_update
    
    if last_len_update!=len_update:
        if text=='random dog':
            sendPhoto(ids)
            len_update=last_len_update


