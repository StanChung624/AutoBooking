# Requirement
## For release user 
* chromedriver ("https://chromedriver.chromium.org/")

Download link and instruction see [HERE](https://github.com/StanChung624/AutoBooking/releases/tag/v0.3.0-beta).
## For sourcecode user:
* chromedriver ("https://chromedriver.chromium.org/")
* selenium
* pandas

# How to Use
## Import specific restuarant crawler script
`from ReservationScripts.Scripts import InParadise` the __InParadise__ are the crawler script for corresponding restuarant.
## Scripts input
All `Scripts.run(INFO, start_when)` takes 2 input args:
* `INFO` a dict object containing required info for chosen restuarant. If there is item missing, the program will ask for input.
* `start_when` time in the format of "YYYY-mm-dd_HH:MM"

## utility
  DriverSetup package info is put [HERE](https://github.com/StanChung624/DriverSetup).
