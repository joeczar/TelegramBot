import telepot
import time
from sense_hat import SenseHat
from senseHat_commands import handleCommands
sense = SenseHat()


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('got command: %s' % command)

    bot.sendMessage(chat_id, handleCommands(command))
    # bot.sendMessage(chat_id, command)


# get key
key = open('/opt/teleBot')
bot = telepot.Bot(key.read().strip('\n'))
key.close()
bot.message_loop(handle)
print('I am listening')


while 1:
    try:
        time.sleep(10)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        sense.clear()
        exit()
    except:
        print('Other error or exception occured!')
        sense.clear()
        exit()
