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
        tabel_nou = [['Network Destination', 'Netmask', 'Gateway', 'Interface']]    # In noul tabel salvam datele
        if match:
            # print("    IPv4 Route Table RAW    ".center(75, '-'))
            # print(match.group("routing_table"))
            pattern = r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$'    # pattern pt. adrese IP
            for rand in match.group("routing_table").splitlines():    # parcurge datele rand cu rand
                linie = list(filter(lambda element: re.fullmatch(pattern, element), rand.split()))    # extrag adrese IP
                if len(linie) == 0:    # elimin lista goala
                    continue
                elif len(linie) == 3:    # linia cu doar 3 IP-uri are 'On-link' la Gateway
                    linie.insert(2, "On-link")
                tabel_nou.append(linie)    # salvam datele in noul tabel

        # Afisarea rezultatelor
        print("    IPv4 Route Table    ".center(75, '-'))
        print("".center(76, '='))
        for linie in tabel_nou:
            print(linie[0].rjust(19), linie[1].rjust(19), linie[2].rjust(19), linie[3].rjust(19), sep='')
        print("".center(76, '='))


# SystemInformation.ip_getter()
# SystemInformation.cp_usage()
SystemInformation.available_memory()
SystemInformation.routing_table()
