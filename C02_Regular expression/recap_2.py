import os
import re


class SystemInformation:
    @staticmethod
    def ip_getter():
        result = os.popen('ipconfig')
        # print(result.readlines())
        for line in result.readlines():
            pattern = r'IPv4 Address.+: (?P<IP>.*)'
            match = re.search(pattern, line)
            if match:
                print(f"IP: {match.group('IP')}")

    @staticmethod
    def cpu_usage():
        result = os.popen('wmic cpu get loadpercentage')
        # print(result.readlines())
        for line in result.readlines():
            pattern = r"(?P<cpu_usage>\d+)"
            match = re.search(pattern, line)
            if match:
                print(f'CPU: {match.group("cpu_usage")}%')


SystemInformation.ip_getter()
SystemInformation.cpu_usage()
