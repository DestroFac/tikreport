import requests
import time

url = "" #Enter the Request URL from the Reporting here
while True:
    response = requests.get(url)
    response_json = response.json()
    print(response_json)
    time.sleep(2)