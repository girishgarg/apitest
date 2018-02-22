import requests
import json

from nose.tools import assert_true
import requests

def test_related():
    url = 'http://127.0.0.1:5000/post_location'
    header = {"content-type": "application/json"}
    data = {"pincode" : "110009", "latitude" : "0.0", "longitude" : "0.0", "address" : "Connaught Place", "city" : "Sgnr",}
    response=requests.post(url,data=json.dumps(data),headers=header)
    assert_true(response.ok)


   
