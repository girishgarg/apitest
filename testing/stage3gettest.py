import json
from nose.tools import assert_true
import requests

def test_related3():
    url = 'http://127.0.0.1:5000/get_location'
    header = {"content-type": "application/json"}
    data = {"latitude" : "28.459497", "longitude" : "77.026638",}
    response=requests.post(url,data=json.dumps(data),headers=header)
    assert_true(response.ok)

