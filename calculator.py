import requests
import json
from pprint import pprint
import os

#1091584118

token=os.environ["TOKEN"]
ids=1091584118


def reply_markup(ids):
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    p={
        "chat_id":ids,
        "text":"calculator",
        "reply_markup":{
            "keyboard":[ [{"text":'7'},{"text":'8'},{"text":'9'},{"text":'*'}], [{"text":'4'},{"text":'5'},{"text":'6'},{"text":'/'}],
             [{"text":'1'},{"text":'2'},{"text":'3'},{"text":'-'}], [{"text":'0'},{"text":'.'},{"text":'='},{"text":'+'}] ],
            "resize_keyboard":True
        }
    }
    res=requests.post(url,json=p)
    return res.json()

reply_markup(ids)