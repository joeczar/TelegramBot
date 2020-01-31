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
    if command[0].isdigit():
        for i, rgb in enumerate(command):
            val = int(rgb)
            if val >= 0 and val <= 255:
                command[i] = val
                print('RGB: ', val)
            else:
                print('rgb int fail')
        return command
    else:
        return
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
            color = parseRGB(command)
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
    parseCommand = command.lower().split()
    if parseCommand[0] == 'blinkt':
        # pop blinkt from array to send only color commands
        parseCommand.pop(0)
        # check if length is 1 and send only value (not an array)
        if len(parseCommand) < 2:
            print(parseCommand[0])
            bot.sendMessage(chat_id, "Got it, " + command, blinktAll(parseCommand[0]))
        else:
            bot.sendMessage(chat_id, "Got it, " + command, blinktAll(parseCommand))

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
