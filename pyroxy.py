import calendar
import time
import json
import re 
from requests import get
from datetime import datetime

now = datetime.now()
dt = now.strftime("%Y-%m-%d-%H-%M")


ts = calendar.timegm(time.gmtime()) * 1000
source_base_link = f'https://api.openproxy.space/list?skip=0&ts={ts}'
proxy_types = ["HTTP", "SOCKS4", "SOCKS5"]
pattern = re.compile(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+') 

print(
"""
╔═╗ ┬ ┬ ╦═╗ ┌─┐ ─┐ ┬ ┬ ┬
╠═╝ └┬┘ ╠╦╝ │ │ ┌┴┬┘ └┬┘
╩    ┴  ╩╚═ └─┘ ┴ └─  ┴  
Version 0.1
`Tiny Proxy Scrapper`

Coded By OptimOS Prime
Telegram : @OptimOSPrime
GitHub   : github.com/mfcharaf
"""
)

proxy_type = int(input("""
Proxy type ?
[1] - HTTP/S
[2] - SOCKS4
[3] - SOCKS5
""")) - 1

print(f'Searching for {proxy_types[proxy_type]}, please wait ...')

json_data = get(source_base_link).content
loaded_json = json.loads(json_data)
filename = f'{proxy_types[proxy_type]}-{dt}.txt'

sum = 0

for x in loaded_json:
     if proxy_types[proxy_type] in x['title']:
          link = f'https://openproxy.space/list/{x["code"]}'
          source = get(link).content
          proxy_list = re.findall(pattern, str(source))
          sum += len(proxy_list)
          f=open(filename,'a+')
          for ip_port in proxy_list:
               f.write(ip_port+'\n')
          f.close()

print(f'{sum} proxies were found')
print(f'Proxy list saved as `{filename}`')
input("\nPress any key to exit")