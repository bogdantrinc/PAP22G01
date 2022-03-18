import os
import re
class SystemInformation:
    @staticmethod
    def ip_getter():
        result=os.popen('ipconfig')
        for line in result.readlines():
            pattern = "IPv4 Address.*: (?P<IP>.*)"
            match=re.search(pattern,line)
            if match:
                print(match.group("IP"))
    @staticmethod
    def cp_usage():
        result1=os.popen('wmic cpu get loadpercentage')
        for line in result1.readlines():
            pattern = "(?P<cpu_usage>\d+)"
            match1=re.search(pattern,line)
            if match1:
                print(match1.group("cpu_usage"))

SystemInformation.ip_getter()

SystemInformation.cp_usage()