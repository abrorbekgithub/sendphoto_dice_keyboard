import requests
import json
from pprint import pprint
import os


url=f'https://dog.ceo/api/breeds/image/random'
res=requests.get(url)
data=res.json()
pprint(data)