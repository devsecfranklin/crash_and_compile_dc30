import requests
import http.client
import json

site = "dc30.crashandcompile.org"
connection = http.client.HTTPSConnection(site)

GUID = "c16e0ad9-240d-4253-998c-70a2d772144b"

# prob set gen
# GET /api/problem_2_a0x90bs/easy/question_sample?guid=bfc78a80-2523-0d0b-bd36-94e8ef3c2b1f

#connection.request('GET', '/api/problem_2_a0x90bs/easy/question_sample?guid=' + GUID)
response = requests.get('https://' + site + '/api/problem_2_a0x90bs/easy/question?guid=' + GUID)

if response.status_code == 200 and 'application/json' in response.headers.get('Content-Type',''):
    print(response.json())
    data = response.json()

    
    requests.get('https://' + site + '/api/problem_2_a0x90bs/easy/answer?guid=' + GUID + '&token=3bee29b&answer=' + "780253") 