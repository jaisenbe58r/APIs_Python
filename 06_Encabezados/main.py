import requests
import os
import json

if __name__ == '__main__':
    url = "https://httpbin.org/post"
    payload = {'nombre':'Jaime', 'curso':'python', 'nivel':'intermedio'}
    headers = {'Conten-Type':'application/json', 'acces-token':'1234'}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.url)

    if response.status_code == 200:
        # print(response.content)
        headers_response = response.headers #diccionario
        server = headers_response['server']
        print(server)