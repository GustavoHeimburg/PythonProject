import platform
import subprocess
import ipaddress
from   concurrent.futures import ThreadPoolExecutor

import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
rede = '.'.join(local_ip.split('.')[:-1]) + '.'

param = '-n' if platform.system().lower() == 'windows' else '-c'

def ping(ip):
    try:
        output = subprocess.check_output(['ping', param, '1', ip], stderr=subprocess.DEVNULL)
        return ip
    except:
        return None

dispositivos = []

with ThreadPoolExecutor(max_workers=100) as executor:
    futures = [executor.submit(ping, rede + str(i)) for i in range(1, 255)]
    for f in futures:
        result = f.result()
        if result:
            dispositivos.append(result)

print("Dispositivos encontrados na rede:")
for ip in dispositivos:
    print(ip)


