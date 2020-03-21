import requests
import os

if __name__ == '__main__':
    url = "https://httpbin.org/get"
    args = {'nombre':'Jaime', 'curso':'python', 'nivel':'intermedio'}
    
    response = requests.get(url, params = args)

    if response.status_code == 200:
        content = response.content
        print(content)
