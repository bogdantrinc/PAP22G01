"""
Extend existing functionality in of app_2 class SystemInformation to support
 - getting available memory (total, used, free)
 - getting routing table and displaying it as a table
"""
import os
import re


class SystemInformation:
    @staticmethod
    def ip_getter():
        result = os.popen('ipconfig')
        for line in result.readlines():
            pattern = r"IPv4 Address.*: (?P<IP>.*)"
            match = re.search(pattern, line)
            if match:
                print(match.group("IP"))

    @staticmethod
    def cp_usage():
        result = os.popen('wmic cpu get loadpercentage')
        for line in result.readlines():
            pattern = r"(?P<cpu_usage>\d+)"
            match = re.search(pattern, line)
            if match:
                print(match.group("cpu_usage"))

    @staticmethod
    def available_memory():
        result = os.popen('systeminfo')
        for line in result.readlines():
            pattern = r"Total Physical Memory:\s+(?P<max_memory>.*)|Available Physical Memory:\s+(?P<available_memory>.*)"
            match = re.search(pattern, line)
            if match:
                print(match.string.strip())

    @staticmethod
    def routing_table():
        result = os.popen('route print')
        pattern = r"IPv4 Route Table\n(?P<routing_table>[^\r\n]+((\r|\n|\r\n)[^\r\n]+)*=)"
        match = re.search(pattern, result.read())
        if match:
            print("    IPv4 Route Table    ".center(75, '-'))
            print(match.group("routing_table"))


# SystemInformation.ip_getter()
# SystemInformation.cp_usage()
SystemInformation.available_memory()
SystemInformation.routing_table()
