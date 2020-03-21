import requests
import os
import json


client_id = 'xxxx'
client_secret = 'xxxx'

code='xxx'

if __name__ == '__main__':

    url = 'https://github.com/login/oauth/access_token'
    payload = {'client_id': client_id, 'client_secret':client_secret, 'code': code}
    headers = {'Accept': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json = response.json()

        access_token = response_json['access_token']
        print(access_token)

    else:
        print(response.status_code)


