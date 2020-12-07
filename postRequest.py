import requests

url = "https://www.google.com/"

payload = {}
files = {}
headers = {
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text)
