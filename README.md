geekbooth
=========
A python program to create a photobooth to replicate the photos for the http://geekthelibrary.org/ program.<br>
It uses the following parts, modules, raspbian packages, and fonts.

# Table of Contents
*[Usage](#usage)<br>
*[Parts](#parts)<br>
*[Font File](#fontfile)<br>
*[Raspbian Package](#raspbianpackage)<br>
*[Python Modules](#pythonmodules)<br>

# <a name="usage"></a>Usage
Press the big GO button<br>
It asks what you geek on the LCD character display.<br>
Give an answer and hit enter.<br>
Hit tells you to enter again to take your pic.<br>
Camera preview shows up on LCD screen for you to frame up.<br>
It snapps the photo and adds the text below it.<br>
It then saves it to the thumbdrive and shows a final image on the LCD screen.<br>
It now waits for the next person to press the GO button to start again.<br>

# <a name="parts"></a>Parts
Raspberry Pi<br>
Raspberry Pi Camera Module<br>
4.3'' Color TFT LCD with composite input<br>
Adafruit RGB Positive LCD http://www.adafruit.com/products/1115 <br>
Powered USB Hub<br>
Thumbdrive to store photos<br>
USB Keyboard<br>
A big button to trigger the GPIO pin to start the photobooth.<br>


# <a name="fontfile"></a>Font File
American Typewriter True Type Font<br>

# <a name="raspbianpackage"></a>Raspbian Packages
usbmount (to auto mount the thumbdrive)<br>

# <a name="pythonmodules"></a>Python Modules
time<br>
subprocess<br>
PIL (Python Image Library)<br>
RPi.GPIO<br>
os<br>
getpass (I'm not using it at the moment)<br>
Adafruit_CharLCDPlate<br>



