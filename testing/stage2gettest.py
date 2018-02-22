import json
from nose.tools import assert_true
import requests

def test_related1():
    url = 'http://127.0.0.1:5000/get_using_postgres'
    header = {"content-type": "application/json"}
    data = {"latitude" : "28.6333", "longitude" : "77.2167",}
    response=requests.post(url,data=json.dumps(data),headers=header)
    assert_true(response.ok)

def test_related2():
    url = 'http://127.0.0.1:5000/get_using_self'
    header = {"content-type": "application/json"}
    data = {"latitude" : "28.6333", "longitude" : "77.2167",}
    response=requests.post(url,data=json.dumps(data),headers=header)
    assert_true(response.ok)



