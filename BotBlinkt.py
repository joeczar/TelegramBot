import sys
import time
import telepot
from blinkt import set_brightness, set_all, set_pixel, show, clear

# clear the LEDs
bright = 0.1
set_brightness(bright)
clear()
show()

helpMessage = 'I can change colors with the commands, "red", "blue", "green" or "white". \n \nI also understand RGB values with "Blinkt R G B" where R, G and B are values from 0 to 255. \n \nYou can turn off the lights with "clear" and set the brightness with "bright" and a number between 0 and 100'

def setBrightness(value, bright):
    # check that value is between 0 and 100
    if value >= 0 and value <= 100:
        # multiply value by 0.01
        val = float(value) * 0.01
        set_brightness(val)
        show()
               
    else:
        brightMessage = "Please give a number betweeen 0 and 100. \n Example: Bright 50"
        bot.sendMessage(chat_id, brightMessage)
        time.sleep(1.5)
        bot.sendMessage(chat_id, helpMessage)

def parseRGB(command):
    #check if command is number, if not exit
    if command[0].isdigit():
        for i, rgb in enumerate(command):
            val = int(rgb)
            if val >= 0 and val <= 255:
                command[i] = val
            else:
                bot.sendMessage(chat_id, helpMessage)
        return command
    else:
        return

def blinktAll(command):
    clear()
    # Test to see of input is 3 values between 0 and 255
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
    else: 
        bot.sendMessage(chat_id, helpMessage)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Got command: %s' % command)
    parseCommand = command.lower().split()
    # check for help
    if parseCommand[0] == "help":
        bot.sendMessage(chat_id, helpMessage)
    # check for bright
    if parseCommand[0] == "bright":
        if len(parseCommand) > 1:
            value = parseCommand[1]
            bot.sendMessage(chat_id, "Setting brightness to " + str(value), setBrightness(int(value), bright)) 
        else:
            errMessage = "Hmmm... That didn't work"
            print(value, parseCommand)
            bot.sendMessage(chat_id, errMessage)
            bot.sendMessage(chat_id, helpMessage)
    # check for color & clear
    elif parseCommand[0] in ('red', 'blue', 'green', 'white', 'clear'):
        bot.sendMessage(chat_id, "Got it, " + command, blinktAll(parseCommand[0]))
    # check for blinkt 
    elif parseCommand[0] == 'blinkt' and len(parseCommand) > 1:
        # pop blinkt from array to send only color commands
        parseCommand.pop(0)
        # check if length is 1 and send only value (not an array)
        if len(parseCommand) < 2:
            bot.sendMessage(chat_id, "Got it, " + command, blinktAll(parseCommand[0]))
        else:
            bot.sendMessage(chat_id, "Got it, " + command, blinktAll(parseCommand))
    else:
        message ='I don\'t understand ' + command
        
        print(message)
        bot.sendMessage(chat_id, message)
        time.sleep(1)
        bot.sendMessage(chat_id, helpMessage)


#get key
key = open('/opt/teleBot')

bot = telepot.Bot(key.read().strip('\n'))
key.close()
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
