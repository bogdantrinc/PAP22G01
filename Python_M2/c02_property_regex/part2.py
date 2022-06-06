import re


my_ips = r"""
Windows IP Configuration


Ethernet adapter Ethernet:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Local Area Connection* 1:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Local Area Connection* 10:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter WiFi:

   Connection-specific DNS Suffix  . : home
   Link-local IPv6 Address . . . . . : fe80::3147:9117:2f32:48ef%22
   IPv4 Address. . . . . . . . . . . : 192.168.0.228
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.0.1

Ethernet adapter Bluetooth Network Connection 3:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Ethernet adapter vEthernet (WSL):

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::10db:50ca:24c5:9579%43
   IPv4 Address. . . . . . . . . . . : 172.28.240.1
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :

Ethernet adapter vEthernet (BluestacksNxt):

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::b5a0:e16e:dcc4:c400%52
   IPv4 Address. . . . . . . . . . . : 172.28.176.1
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :
"""
pattern = "IPv4 Address.*: (.*)"

result = re.findall(pattern, my_ips)
print(result)
pattern = "IPv4 Address.*: (?P<IP>.*)"
result = re.search(pattern, my_ips)
print(result.group("IP"))
print(result)