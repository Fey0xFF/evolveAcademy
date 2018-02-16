import requests
import pprint

url = "http://httpbin.org/ip"
ip = requests.get(url).json()
print(ip['origin'])
