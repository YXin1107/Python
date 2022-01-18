import requests
r = requests.get('http://www.bilibili.com')
print(r.text)
