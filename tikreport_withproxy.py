import requests
import random
from bs4 import BeautifulSoup
import time


with open("valid_proxies.txt", "r") as f:
    proxies = f.read().split("\n")

counter = 0

url = ""    #Enter the Request URL from the Reporting here


for site in url:
    try:
        print(f"Current Proxy:: {proxies[counter]}")
        response = requests.get(url, proxies={"http": proxies[counter],
                                          "https": proxies[counter]})
        response_json = response.json()
        print(response_json)
    except:
        print("Proxy not working")
    finally:
        counter+= 1

    



