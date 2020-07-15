import requests
import os
speed = ''
username = ''
password = ''
session = requests.Session()
ntapi = "https://www.nitrotype.com/api/"
headers = {'Content-Type':'application/x-www-form-urlencoded'}
def login(username,password):
    data = {"username": username,"password": password}
    url = f"{ntapi}login"
    login = session.post(url,data=data)
    return login
def get_uhash(username,password):
    login(username,password)
    uhash = session.cookies["ntuserrem"]
    return uhash
def reset_race_speed(uhash):
    url = f"{ntapi}race/save-qualifying"
    data = f"speed={speed}&accuracy=100&carID=15&raceSounds=off&uhash={uhash}"
    post = session.post(url=url,data=data,headers=headers).json()
    if post["success"]:
        return "success"
    else:
        return post["data"]
print(reset_race_speed(get_uhash(username, password)))
