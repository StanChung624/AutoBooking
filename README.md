# Requirement
## for release ver. user (yet to be published)
    * chromedriver ("https://chromedriver.chromium.org/")
## for sourcecode user:
    * chromedriver ("https://chromedriver.chromium.org/")
    * selenium
    * pandas

# How to Use
## Import specific restuarant crawler script
'from ReservationScripts.Scripts import InParadise' the __InParadise__ are the crawler script for corresponding restuarant.
## Scripts input
All scripts takes 2 input args:
* INFO:  a dict object containing required info for chosen restuarant. If there is item missing, the program will ask for input.
* start_when: time in the format of "YYYY-mm-dd_HH:MM"
