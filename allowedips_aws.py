import json
import urllib.request

url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
link = urllib.request.urlopen(url)
f = link.read()
ip = json.loads(f)
for i in ip['prefixes']:
    print('AllowedIPs =', i['ip_prefix'])
