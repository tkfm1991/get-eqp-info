from ntc_templates.parse import parse_output
from pprint import pprint

output="""
username@pcname:~$ ifconfig
eno1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
wlp58s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet ***.***.***.***  netmask 255.255.255.0  broadcast ***.***.***.255
        inet6 fe80::****:****:****:****  prefixlen 64  scopeid 0x20<link>
        ether **:**:**:**:**:**  txqueuelen 1000  (イーサネット)
        RX packets 10262  bytes 3310613 (3.3 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3723  bytes 448699 (448.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eno2: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1400
username@pcname:~$
"""

parsed = parse_output(platform="ubuntu", command="ifconfig", data=output)
pprint(parsed)