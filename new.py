import requests
import json
import os
from pprint import pprint

token=os.environ["TOKEN"]    #1

def getUpdates():          #2
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    res=requests.get(url=url)
    update=res.json()["result"]
    return update[-1]

def ids_text():       #3
    ids=getUpdates()["message"]["from"]["id"]
    text=getUpdates()["message"]["text"]
    return ids,text

def randomPhoto():        #4
    url=f'https://dog.ceo/api/breeds/image/random'
    res=requests.get(url)   
    img_url=res.json()["message"]
    return img_url

def reply_markup(chat_id):    #5
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    p={
        "chat_id":chat_id,
        "text":"Dogs",
        "reply_markup":{
            "keyboard":[[{"text":"random dog"}]],
            "resize_keyboard":True
        }
    }
    res=requests.post(url,json=p)
    return res.json()



