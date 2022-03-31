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
        result = os.popen('systeminfo').read()
        pattern = r"(Total Physical Memory:\s+(?P<max_memory>.*))\n(Available Physical Memory:\s+(?P<available_memory>.*))"
        match = re.search(pattern, result)
        if match:
            max_memory = match.group("max_memory")
            available_memory = match.group("available_memory")
            used_memory = str(int(max_memory[:-3].replace(',', '')) - int(available_memory[:-3].replace(',', ''))) + ' MB'
            print("Total Physical Memory: ", max_memory)
            print("Used Physical Memory: ", used_memory)
            print("Available Physical Memory: ", available_memory)

    @staticmethod
    def routing_table():
        result = os.popen('route print').read()
        pattern = r"IPv4 Route Table\n(?P<routing_table>[^\r\n]+((\r|\n|\r\n)[^\r\n]+)*=)"
        match = re.search(pattern, result)
        if match:
            print("    IPv4 Route Table    ".center(75, '-'))
            print(match.group("routing_table"))


# SystemInformation.ip_getter()
# SystemInformation.cp_usage()
SystemInformation.available_memory()
SystemInformation.routing_table()
