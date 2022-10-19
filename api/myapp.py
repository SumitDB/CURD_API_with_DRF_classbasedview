import requests
import json

URL="http://127.0.0.1:8000/studentapi/"

#read
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url= URL, data = json_data)
    data = r.json()
    print(data)

#create
def post_data():
    data = {'name':'Ravi','roll':104,'city':'Mumbai'}
    json_data = json.dumps(data)
    r = requests.post(url= URL, data = json_data)
    data = r.json()
    print(data)

#update
def update_data():
    data = {'id':4,'name':'Ravii','roll':104,'city':'Indoreee'}
    json_data = json.dumps(data)
    r = requests.put(url= URL, data = json_data)
    data = r.json()
    print(data)

#delete
def delete_data():
    data = {'id':3}
    json_data = json.dumps(data)
    r = requests.delete(url= URL, data = json_data)
    data = r.json()
    print(data)
get_data()
