geekbooth
=========
A python program to create a photobooth to replicate the photos for the http://geekthelibrary.org/ program.
It uses the following parts, modules, raspbian packages, and fonts.

*[Usage](#usage)
Press the big GO button
It asks what you geek.
Give an answer and hit enter.
Hit tells you to enter again to take your pic.
Camera preview shows up on LCD screen for you to frame up.
It snapps the photo and adds the text below it.
It then saves it to the thumbdrive and shows a final image on the LCD screen.
It now waits for the next person to press the GO button to start again.

*[Parts](#parts)
Raspberry Pi
Raspberry Pi Camera Module
4.3'' Color TFT LCD with composite input
Adafruit RGB Positive LCD http://www.adafruit.com/products/1115 
Powered USB Hub
Thumbdrive to store photos
USB Keyboard
A big button to trigger the GPIO pin to start the photobooth.


*[Font File](#fontfile)
American Typewriter True Type Font

*[Raspbian Package](#raspbianpackage)
usbmount (to auto mount the thumbdrive)

*[Python Modules](#pythonmodules)
time
subprocess
PIL (Python Image Library)
RPi.GPIO
os
getpass (I'm not using it at the moment)
Adafruit_CharLCDPlate



