# Regular expressions: https://regex101.com/
import re

my_ips = r"""Microsoft Windows [Version 10.0.19044.1586]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Bogdan>ipconfig

Windows IP Configuration


Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . :
   IPv6 Address. . . . . . . . . . . : 2a02:a58:80e6:5300:6105:e57c:b119:e35b
   Temporary IPv6 Address. . . . . . : 2a02:a58:80e6:5300:ed6b:d2d6:7acc:5a12
   Link-local IPv6 Address . . . . . : fe80::6105:e57c:b119:e35b%15
   IPv4 Address. . . . . . . . . . . : 192.168.100.4
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : fe80::1%15
                                       192.168.100.1

Wireless LAN adapter Local Area Connection* 1:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Local Area Connection* 2:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Wi-Fi:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Ethernet adapter Bluetooth Network Connection:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

   IPv4 Address. . . . . . . . . . . : 192.168.112.69
C:\Users\Bogdan>"""

pattern = 'IPv4 Address.+: (.*)'

result = re.findall(pattern, my_ips)
print(result)
# result = re.search(pattern, my_ips)
# print(result)

pattern = 'IPv4 Address.+: (?P<IP>.*)'
result = re.search(pattern, my_ips)
print(result.group('IP'))
print(result.groupdict())
