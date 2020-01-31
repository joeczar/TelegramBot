import sys
import time
import telepot
import re
from blinkt import set_brightness, set_all, set_pixel, show, clear

# clear the LEDs
set_brightness(0.1)
clear()
show()

# define message
err = ''

def msgRecievedBlinkt():
    pixel = 8
    clear()
    while pixel > 0:
        set_pixel(pixel-1, 0, 0, 255)
        show()
        time.sleep(0.5)
        pixel - 1


def parseRGB(command):
    #check if command is number, if not exit
    regexTest = re.search
    #if number split to sest for RGB values, raise exception if number outside of RGB values

    # try:
    #     regexTest = re.search("\d{3} \d{3} \d{3}", command)
    #     print('regexTest:', regexTest)
    #     if regexTest is not None:
    #         color = re.split("\s", command)
    #         for i, c in enumerate(color):
    #             # test that the value is a number from 0 to 255
    #             try:
    #                 c = re.search("\d|\d{2}|\d{3}", c)
    #                 print('before if', c)
    #                 if c is not None and len(c) <= 3:
    #                     color[i] = c
    #                     print(c)
    #                 else:
    #                     err = "Please give RGB values between 0 and 255 (0, 128, 128)."
    #                     raise Exception(err)
    #             except:
    #                 return err
    #         print(color)            
    #         return color
    # except:
    #     print(err)



def blinktAll(command):
    clear()
    # Test to see of input is 3 values between 0 and 255
    print(parseRGB(command))
    try:
        if command == "red":
            color = [255, 0, 0]
        elif command == "green":
            color = [0, 255, 0]
        elif command == "blue":
            color = [0, 0, 255]
        elif command == "white":
            color = [255, 255, 255]    
        elif command == "clear":
            color = [0, 0, 0]
        else:
            parseRGB(command)
            #print(color)
            
        if color is not None:
            r = color[0]
            g = color[1]
            b = color[2]
            clear()
            set_all(r, g, b)
            show()
            

    except:
        print('ERROR:', err)


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Got command: %s' % command)
    # if command is True:
    # msgRecievedBlinkt()
    
    bot.sendMessage(chat_id, "Blinkt " + command, blinktAll(command.lower()))

#get key
key = open('/opt/teleBot')

bot = telepot.Bot(key.read().strip('\n'))
bot.message_loop(handle)
print('I am listening...')

while 1:
    try:
        time.sleep(10)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        exit()

    except:
        print('Other error or exception occured!')
