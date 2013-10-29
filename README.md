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
*[Install Log for Raspbian](#installlog)<br>

# <a name="usage"></a>Usage
Press the big GO button<br>
It asks what you geek on the LCD character display.<br>
Give an answer and hit enter.<br>
Hit tells you press the flashing red button to take your pic.<br>
Camera preview shows up on LCD screen for you to frame up.<br>
It snapps the photo and adds the text below it.<br>
It then saves it to the thumbdrive and shows a final image on the LCD screen.<br>
It now waits for the next person to press the GO button to start again.<br>

# <a name="parts"></a>Parts
Raspberry Pi<br>
Raspberry Pi Camera Module<br>
4.3'' Color TFT LCD with composite input<br>
Adafruit RGB Positive LCD http://www.adafruit.com/products/1115 <br>
Adafruit Red LED Button http://www.adafruit.com/products/1439 <br>
Powered USB Hub<br>
Thumbdrive to store photos<br>
USB Keyboard<br>


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

# <a name="installlog"></a> Raspbian Install Log
This is just a log of things I did after I installed Raspbian<br>
<br>
Installed Raspbian.<br>
<br>
Installed fim to view images on the command line.<br>
sudo apt-get install fim<br>
<br>
edited /etc/modules and added the following for the LCD board<br>
        i2c-bcm2708<br>
        i2c-dev<br>
sudo apt-get install python-smbus<br>
sudo apt-get install i2c-tools<br>
<br>
Make sure the 20 is there to identify the board.<br>
sudo i2cdetect -y 1<br>
<br>
made sure git was installed<br>
sudo apt-get install git<br>
<br>
installed code for the LCD<br>
git clone https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git<br>
<br>
Installed GPIO tools<br>
sudo apt-get install python-dev<br>
sudo apt-get install python-rpi.gpio<br>
<br>
Installed pip to be able to install python libraries.<br>
sudo apt-get install python-setuptools<br>
sudo easy_install pip<br>
<br>
Installed some python libraries I need<br>
sudo apt-get install python-imaging<br>
<br>
copied the python code for the LCD plate to the working directory for my script<br>
cp ~/myprojects/adafruit/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate/* to ?<br>
<br>
<br>
Make USB thumbdrive automount when inserted:<br>
apt-get install usbmount<br>
<br>

