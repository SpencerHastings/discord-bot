from datetime import datetime
import requests
import json

def get_time():
    now = datetime.now()
    currenttime = now.strftime("%m/%d/%Y, %H:%M:%S")
    return currenttime

def get_bitcoin():
    request = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url = request)
    data = response.json()
    price = data["bpi"]["USD"]["rate"]
    return price