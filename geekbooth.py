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
GPIO.setup(22,GPIO.IN) #GO Button
GPIO.setup(18,GPIO.OUT, initial=GPIO.LOW) #GO Button LED

lcd = Adafruit_CharLCDPlate()
font = ImageFont.truetype("./at.ttf",130) #full frame

os.system("clear")

gbversion = "  geek.booth.\n"

def flashlights():
    col = (lcd.RED , lcd.YELLOW, lcd.GREEN, lcd.TEAL,
           lcd.BLUE, lcd.VIOLET)
    for c in col:
        lcd.backlight(c)
        time.sleep(.25)
    lcd.backlight(lcd.GREEN)

# Watch GO button for press
def gowatcher():
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
                lcd.message("Hit GO Button!")


# Morse Code Blinkn Light
def barker():
    CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
            'D': '-..',    'E': '.',      'F': '..-.',
            'G': '--.',    'H': '....',   'I': '..',
            'J': '.---',   'K': '-.-',    'L': '.-..',
            'M': '--',     'N': '-.',     'O': '---',
            'P': '.--.',   'Q': '--.-',   'R': '.-.',
            'S': '...',    'T': '-',      'U': '..-',
            'V': '...-',   'W': '.--',    'X': '-..-',
            'Y': '-.--',   'Z': '--..',

            '0': '-----',  '1': '.----',  '2': '..---',
            '3': '...--',  '4': '....-',  '5': '.....',
            '6': '-....',  '7': '--...',  '8': '---..',
            '9': '----.'
            }
    msg = "GO"
#    print(msg + "\n")
#    time.sleep(1)
    for char in msg:
        gowatcher()
        time.sleep(.40)
        for dotdash in CODE[char.upper()]:
            pulse = 0
            gowatcher()
            if dotdash == str("-"):
                pulse = .10
            else:
                pulse = .05
            GPIO.output(18,GPIO.HIGH)
            print(dotdash)
            time.sleep(pulse)
            GPIO.output(18,GPIO.LOW)
            time.sleep(.20)



# Taking the photo.
def grab_cam():
    lcd.clear()
    lcd.message("    LOOK UP\n")
    lcd.message("   AND SMILE!")
    time.sleep(2)
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
    lcd.message(" Picture Taken.\n")
    lcd.message("Adding Your Geek.")
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
#    os.system("fim -c '45%; sleep \"5\"; q'" + " " + str(filename)) #vga monitor
    os.system("fim -c '20%; sleep \"5\"; q'" + " " + str(filename)) #composite LCD screen
    lcd.clear()
    lcd.backlight(lcd.VIOLET)
    lcd.message("    All Done\n")
    lcd.message("   Thank You!")

def mainrun():
    # Cycle through backlight colors
    col = (lcd.RED , lcd.YELLOW, lcd.GREEN, lcd.TEAL,
           lcd.BLUE, lcd.VIOLET)
    for c in col:
        lcd.backlight(c)
        time.sleep(.25)

    global filename
    filename = "/media/usb0/geek" + str(time.strftime("%Y%m%d-%H%M%S")) + ".jpg"
    lcd.clear()
    lcd.backlight(lcd.GREEN)
    lcd.message("Type What U Geek\n")
    lcd.message(" Then Hit Enter")
    os.system("clear")
    global whatgeek
    whatgeek = str(raw_input("What do you geek?  ")) # Get what they geek
    #whatgeek = str(getpass.getpass(prompt="")) #hides text input to LCD screen
    lcd.clear()
    lcd.backlight(lcd.YELLOW)
    lcd.message("Nice! You Geek:\n")
    lcd.message("%s" % whatgeek)
    time.sleep(2)
    lcd.clear()
    lcd.message("  Press Button\n")
    lcd.message("  To Take Pic")
    while True:
        GPIO.output(18,GPIO.HIGH)
        time.sleep(.1)
        GPIO.output(18,GPIO.LOW)
        if (GPIO.input(22) == False ):
            GPIO.output(18,GPIO.HIGH)
            grab_cam()
            break
        time.sleep(.1)
    addgeek()

lcd.clear()
lcd.message(gbversion)
lcd.message("Hold GO Button!")
flashlights()
print(gbversion)
print("Ready To Go")


# Run the program
try:
    while True:
        barker()
except:
# LCD Cleanup when done
    lcd.clear()
    lcd.backlight(lcd.OFF)
    GPIO.cleanup()
