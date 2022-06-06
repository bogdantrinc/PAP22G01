## Exam Python M2

Create Python UI application that will retrieve all timezones from this link http://worldtimeapi.org/api/timezone/Europe and two random number from https://csrng.net/csrng/csrng.php?min=1&max=2116:
The application must randomly select 2 time zones based on the retrieved numbers and when the "Compare" button is pushed the time difference will be displayed
UI implementation ()
Detailed description:
  - Pylint shows no errors or warnings (10p)
  - At least one unittest created for at lest one function (10p)
    - recommended for function to get/calculate random number 
  - File menu has Close option which will close the application (10p)
  - UI has 2 fields with timezones, one compare button and one field for time difference (30p)
  - Time difference is correctly displayed when the "Compare" button is pressed (20p)
  - Retrieving timezones or random numbers is done in parallel (20p)

Layout 
```
##################################
# Timezone1 # Timezone2 # Result #
##################################
#        Compare Button          #
##################################
```
