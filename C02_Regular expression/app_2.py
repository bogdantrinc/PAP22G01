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
    def cpu_usage():
        result = os.popen('ipconfig')
        for line in result.readlines():
            pattern = "IPv4 Address.*: (?P<IP>.*)"
            match = re.search(pattern, line)
            if match:
                print(match.group("IP"))

SystemInformation.ip_getter()