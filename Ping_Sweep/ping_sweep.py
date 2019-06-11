# -*- coding: utf-8 -*-
import subprocess
import ipaddress
from subprocess import DEVNULL

net_addr = input("Enter the network address in CIDR format(for example, 10.1.1.0/16): ")

ip_net = ipaddress.ip_network(net_addr)
all_hosts = list(ip_net.hosts())
info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

ping = {ping_ip: subprocess.Popen(['ping', '-n', '1', '-w', '500', str(ping_ip)], stdout=DEVNULL) for ping_ip in ip_net.hosts()}

up_ip_list = []

while ping:
    for ip, proc in ping.items():
        if proc.poll() is not None:
            del ping[ip]
            if proc.returncode == 0:
                unsorted_list = list.append(up_ip_list, ip)
            elif proc.returncode == 1:
                pass
            else:
                print('%s error' % ip)
            break

for result in sorted(up_ip_list):
    print('%s is up' % result)
