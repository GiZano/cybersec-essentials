import requests

response = requests.get("http://web-01.challs.olicyber.it/")

print(response.text)