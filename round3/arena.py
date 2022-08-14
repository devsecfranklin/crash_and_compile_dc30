import requests
import http.client
import json

site = "dc30.crashandcompile.org"
connection = http.client.HTTPSConnection(site)

GUID = "c16e0ad9-240d-4253-998c-70a2d772144b"

# prob set gen
# GET /api/arena_b9trs9s/check_sample?guid= GUID

response = requests.get('https://' + site + '/api/arena_b9trs9s/check?guid=' + GUID)

my_token = ""
this_list = []
if response.status_code == 200 and 'application/json' in response.headers.get('Content-Type',''):
    #print(response.json())
    data = response.json()

    counter = 0
    token = data[-1]
    print("THe token is: {}".format(token))
    for thing in data:
        this_list.append(data[counter])
        print ("found: {}".format(data[counter]))
        counter += 1

    


    for key, value in token.items():
        print (value)
        my_token = value
    
    
    #requests.get('https://' + site + '/api/problem_2_a0x90bs/easy/answer?guid=' + GUID + '&token=3bee29b&answer=' + "780253") 
#GET /api/arena_b9trs9s/move_sample?guid=bfc78a80-2523-0d0b-bd36-94e8ef3c2b1f&token=a0a70b8&move=N
response = requests.get('https://' + site + '/api/arena_b9trs9s/move?guid=' + GUID 
                        + '&token='
                        + my_token 
                        + '&move=' + "W") 

if response.status_code == 200 and 'application/json' in response.headers.get('Content-Type',''):
    print(response.json())

# Board status request
print ("Show board status")
# GET /api/arena_b9trs9s/board_sample?guid=bfc78a80-2523-0d0b-bd36-94e8ef3c2b1f
response = requests.get('https://' + site + '/api/arena_b9trs9s/check?guid=' + GUID)

if response.status_code == 200 and 'application/json' in response.headers.get('Content-Type',''):
    print(response.json())