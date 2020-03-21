import requests
import os
import json

if __name__ == '__main__':
    url = "https://httpbin.org/post"
    payload = {'nombre':'Jaime', 'curso':'python', 'nivel':'intermedio'}
    
    response = requests.post(url, data = json.dumps(payload))

    if response.status_code == 200:
        print(response.content)