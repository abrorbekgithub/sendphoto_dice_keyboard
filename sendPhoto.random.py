import requests
import json
from pprint import pprint
import os

#1091584118
#'https://random.dog/85ca20a7-e792-4166-8709-1e0710b6d68d.jpg'
#'https://random.dog/53549b25-0201-4d08-a792-f05f0c78f1fd.mp4'

token=os.environ["TOKEN"]
ids=1091584118

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

sendPhoto(ids)
