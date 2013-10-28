import time 
import subprocess 
import PIL 
from PIL import ImageFont 
from PIL import Image 
from PIL import ImageDraw 
import RPi.GPIO as GPIO 
import os 
import getpass 
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.IN)
GPIO.setup(15,GPIO.IN)

lcd = Adafruit_CharLCDPlate()
font = ImageFont.truetype("./at.ttf",130) #full frame

os.system("clear")

gbversion = "LPL GeekBooth!\n"

def flashlights():
    col = (lcd.RED , lcd.YELLOW, lcd.GREEN, lcd.TEAL,
           lcd.BLUE, lcd.VIOLET)
    for c in col:
        lcd.backlight(c)
        time.sleep(.25)
    lcd.backlight(lcd.GREEN)

# Taking the photo.
def grab_cam():
    time.sleep(1)
    lcd.clear()
    lcd.message("COUNTDOWN:\n")
    lcd.message("          3")
    time.sleep(1)
    lcd.clear()
    lcd.message("COUNTDOWN:\n")
    lcd.message("          2")
    time.sleep(1)
    lcd.clear()
    lcd.message("COUNTDOWN:\n")
    lcd.message("          1")
    time.sleep(1)
    lcd.clear()
    lcd.message("     SMILE!")
    ##print "SMILE!!"
    subprocess.Popen("raspistill -fp -t 2000 -o ./temp.jpg", shell=True)
    time.sleep(4)
    lcd.clear()
    lcd.message("      SNAP!")
    ##print "SNAP"



# Adding the text to the picture.
def addgeek(): 
    webcamphoto = Image.open(open("./temp.jpg",'rb'))
    time.sleep(4)
    lcd.backlight(lcd.GREEN)
    lcd.clear()
    lcd.message(" Picture Taken\n")
    lcd.message("Adding Your Geek")
    ##print "Photo is taken... adding text."
    draw = ImageDraw.Draw(webcamphoto)
    draw.rectangle([(0,1620),(2592,1944)],fill = '#000000')  #2592x1944 full frame
    draw.text((20,1640),"I",(255,255,255),font = font)
    draw.text((90,1640),"geek",(255,0,0),font = font)
    draw.text((20,1770),whatgeek,(255,255,255),font = font)
    lcd.clear()
    lcd.message(" Saving Image")
    ##print "Saving image."
    time.sleep(1)
    lcd.clear()
    lcd.message(" Check Out Your\n")
    lcd.message("    Preview")
    webcamphoto.save(filename)
    ##print "Done!"
#    os.system("fim -c '45%; sleep \"5\"; q'" + " " + str(filename)) #vga
    os.system("fim -c '20%; sleep \"5\"; q'" + " " + str(filename)) #composite
    lcd.clear()
    lcd.backlight(lcd.VIOLET)
    lcd.message("    All Done\n")
    lcd.message("   Thank You!")

def mainrun():
    # Cycle through backlight colors
    col = (lcd.RED , lcd.YELLOW, lcd.GREEN, lcd.TEAL,
           lcd.BLUE, lcd.VIOLET, lcd.ON   , lcd.OFF)
    for c in col:
        lcd.backlight(c)
        time.sleep(.25)

    global filename
    filename = "/media/usb0/geek" + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
    lcd.clear()
    lcd.backlight(lcd.RED)
    lcd.message("What Do U Geek?")
    os.system("clear")
    global whatgeek
    whatgeek = str(raw_input("What do you geek?")) # Get what they geek
    #whatgeek = str(getpass.getpass(prompt="")) #hides text input to screen
    lcd.clear()
    lcd.backlight(lcd.YELLOW)
    lcd.message("Nice! You Geek:\n")
    lcd.message("%s" % whatgeek)
    time.sleep(2)
    lcd.clear()
    lcd.message("Press Enter\n")
    lcd.message("To Take The Pic")
    raw_input() # For debug to pause before snapping

    grab_cam()
    addgeek()

lcd.clear()
lcd.message(gbversion)
lcd.message("Press GO Button!")
flashlights()
print(gbversion)
print("Ready To Go")


# Run the program
try:
    while True:
        time.sleep(0.2)
#        if (GPIO.input(15) == False ):
#            lcd.clear()
#            lcd.backlight(lcd.RED)
#            lcd.message("SHUTTING DOWN")
#            time.sleep(2)
#            lcd.backlight(lcd.OFF)
#            lcd.clear()
#            os.system("sudo shutdown -h now")
        if (GPIO.input(22) == False ):
            if not os.path.ismount("/media/usb0/"):
                lcd.clear()
                lcd.backlight(lcd.RED)
                lcd.message("NO THUMBDRIVE!\n")
                lcd.message(" Insert & Retry")
            else:
                mainrun()
                os.system("clear")
                flashlights()
                lcd.clear()
                lcd.backlight(lcd.GREEN)
                lcd.message(gbversion)
                lcd.message("Press GO Button!")
except:
# LCD Cleanup when done
    lcd.clear()
    lcd.backlight(lcd.OFF)

# Uncomment when running from the terminal to view final image
#os.system("fbi --autodown ./final.jpg")
