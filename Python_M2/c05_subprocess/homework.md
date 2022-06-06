## Quiz

https://www.classmarker.com/

## Homework

Create a class for an object that implement three methods.

- first method gets the latest stable version of python by downloading and looking in the content of this
  page: https://en.wikipedia.org/wiki/History_of_Python
    - To download the page try using the following command for windows
      ```powershell -c "Invoke-WebRequest -Uri 'https://en.wikipedia.org/wiki/History_of_Python' -OutFile 'C:\temp\page.html'"```
      or curl, wget, or some other tools you may have in case of mac.

- the second method downloads the latest version of python and starts the installer
    - no installation steps are required just start the downloaded executable file

- compare the retrieved version with the first 2 digits of your installed version and show a message to the user with
  current and available version.
    - you can get the python version by using the command ```python3 --version```