r"""
Create a class for an object that implement three methods.

- first method gets the latest stable version of python by downloading and looking in the content of this
  page: https://en.wikipedia.org/wiki/History_of_Python
    - To download the page try using the following command for Windows
            powershell -c "Invoke-WebRequest -Uri 'https://en.wikipedia.org/wiki/History_of_Python' -OutFile 'C:\temp\page.html'"
      or curl, wget, or some other tools you may have in case of mac.

- the second method downloads the latest version of python and starts the installer
    - no installation steps are required just start the downloaded executable file

- compare the retrieved version with the first 2 digits of your installed version and show a message to the user with
  current and available version.
    - you can get the python version by using the command
            python3 --version
"""
import os
import re
from subprocess import Popen
from time import sleep


class DoThings:
    def get_version(self):
        Popen(['powershell', '-c', r"Invoke-WebRequest -Uri 'https://en.wikipedia.org/wiki/History_of_Python' -OutFile 'C:\Users\Bogdan\PycharmProjects\PAP22G01\C05_Subprocesses\pagina.html'"])
        sleep(1)
        with open('pagina.html', 'r', encoding='utf8') as fisier:
            for line in fisier.readlines():
                pattern = "<td><i>(?P<version>\d*.\d*.\d*)"
                match = re.search(pattern, line)
                if match:
                    self.latest_version = match.group("version")
        return self.latest_version


    @staticmethod
    def download():
        Popen(['powershell', '-c', r"Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe' -OutFile 'C:\Users\Bogdan\PycharmProjects\PAP22G01\C05_Subprocesses\python-3.10.4-amd64.exe'"])


    def compare(self):
        result = os.popen('python3 --version')
        pattern = "[a-zA-Z]* (?P<version>\d*.\d*.\d*)"
        match = re.search(pattern, result.readline())
        if match:
            self.installed_version = match.group("version")
        self.latest_version = self.latest_version.split('.')
        self.installed_version = self.installed_version.split('.')
        if self.latest_version[0] != self.installed_version[0] or self.latest_version[1] != self.installed_version[1]:
            print("You don't have the latest version!")
        else:
            print("You have the latest version!")
        print("The latest version is: ", ".".join(self.latest_version))
        print("The installed version is: ", ".".join(self.installed_version))


obiect = DoThings()
print("Official Version: ", obiect.get_version())
obiect.download()
obiect.compare()
