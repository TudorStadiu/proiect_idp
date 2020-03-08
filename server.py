import json
import requests
from urllib.request import urlopen

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ('https://jsonplaceholder.typicode.com/todos/1')

text = get_jsonparsed_data(url)
print(text)
