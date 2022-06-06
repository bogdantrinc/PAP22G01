## Exam Python M2

Create Python UI application that will work as a random color screensaver:
* retrieve 3 random numbers every 10 seconds: (50p) 
  * https://csrng.net/csrng/csrng.php?min=0&max=255 
  * create app to run in full screen and apply solid color from the 3 numbers:
    * R = hex of first number 
    * G = hex of second number 
    * B = hex of third number
  * on click the color will refresh automatically
Detailed description:
  - all colors must be retried in parallel (5p)
  - all modules classes and methods must be documented (10p)
  - type hints should be used whenever possible (5p)
  - at least two unittests created for at lest one function (20p)
  - colored window can run full in full screen. (20p)
  - clicking the colored surface automatically updates color (10p)
  - colors are changed every 10 seconds with retrieved random color (30p)

Note: color can be set like #000000 where 00 is 0 and ff is 255
                            #RRGGBB