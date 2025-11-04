import webbrowser
import requests
import json

def chuck():
    f = r"https://api.chucknorris.io/jokes/random"
    data = requests.get(f)
    tt = json.loads(data.text)

    print(tt["value"])

chuck()