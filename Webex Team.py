import requests
import json
from pprint import pprint

#token = 'NWU0NTkzODEtMWJlYS00OTNjLWI4M2MtMmY0YTVjOTNkMGEzOTJlZmFmMDctNTAw_PF84_consumer'


##########  Create a TEAM ##########


url = 'https://api.ciscospark.com/v1/teams'
headers = {'Authorization': f'Bearer {token}',
	   'Content-Type': 'application/json'}
body = {
	'name': 'ABHINAV Team'
}

##post_response = requests.post(
##	url, headers=headers, data=json.dumps(body)).json()
##pprint(post_response)

get_response = requests.get(url, headers=headers).json()
##print(get_response)
teams = get_response['items']
for team in teams:
    if team['name'] == 'ABHINAV Team':
        teamId = team['id']


########## Create a ROOM  ##########

room_url = 'https://api.ciscospark.com/v1/rooms'
room_body = {
    'title': 'ABHINAV Room',
    'teamId': teamId
}


#room_post = requests.post(room_url, headers=headers,
#                          data=json.dumps(room_body)).json()
#pprint(room_post)

get_rooms = requests.get(room_url, headers=headers).json()
rooms = get_rooms['items']

for room in rooms:
    if room['title'] == 'ABHINAV Room':
        roomId = room['id']


##########  Post A Message To The ROOM  ##########

msg_url = 'https://api.ciscospark.com/v1/messages'
msg_body = {
    'roomId': roomId,
    'text': 'Alert: Interface Gigabite 1/24 on device NX-9300 is UP'
}

msg_response = requests.post(
    msg_url, headers=headers, data=json.dumps(msg_body)).json()

