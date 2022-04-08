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
from subprocess import Popen


class DoThings:
    @staticmethod
    def get_version():
        Popen(['powershell', '-c', r"Invoke-WebRequest -Uri 'https://en.wikipedia.org/wiki/History_of_Python' -OutFile 'C:\Users\Bogdan\PycharmProjects\PAP22G01\C05_Subprocesses\pagina.html'"])
        # with open('pagina.html', 'r') as fisier:
        #     print(fisier.read())

    @staticmethod
    def download():
        Popen(['powershell', '-c', r"Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe' -OutFile 'C:\Users\Bogdan\PycharmProjects\PAP22G01\C05_Subprocesses\python-3.10.4-amd64.exe'"])


obiect = DoThings()
obiect.get_version()
