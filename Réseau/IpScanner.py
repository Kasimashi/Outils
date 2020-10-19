#!/usr/bin/python3

import subprocess
import ipaddress
import json
import concurrent.futures

network = ipaddress.ip_network(input("Enter the network to scan : "))
hosts = network.hosts()
active_hosts= {"active_ip_addrs": []}
inactive_hosts= {"inactive_ip_addrs": []}

def pingda(ip_addr):
    try:
        subprocess.check_output(["ping", "-c", "1", ip_addr])
        active_hosts["active_ip_addrs"].append(ip_addr)
    except:
        inactive_hosts["inactive_ip_addrs"].append(ip_addr)


executor = concurrent.futures.ThreadPoolExecutor(254)
ping_hosts = [executor.submit(pingda, str(ip)) for ip in hosts]

json_active_hosts = json.dumps(active_hosts, indent=1)
json_inactive_hosts = json.dumps(inactive_hosts, indent=1)

print(json_active_hosts, json_inactive_hosts)
