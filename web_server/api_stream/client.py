import requests


with requests.get("http://localhost:8000", stream=True) as r:
    for chunk in r.iter_content(100):
        print(chunk)