import sys
import time
import telepot
import subprocess

def teleBash(chat_id, command):
    try:
        completed = subprocess.run(
            command,
            check=True,
            shell=True,
            stdout=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as err:
        print("Error:" + err)
        bot.sendMessage(chat_id, err)
    else:
        returnMessage = 'returncode:', completed.returncode
        stdoutMessage = 'Have {} bytes in {} stdout:\n{}'.format(
            len(completed.stdout), 
            'yer Ma', 
            completed.stdout.decode('utf-8')
            )
        print("return Message", returnMessage)
        print("stdout message", stdoutMessage)
        
        bot.sendMessage(chat_id, completed.stdout.decode('utf-8'))

# def handle(msg):
#     chat_id = msg['chat']['id']
#     command = msg['text']

#     print('runing command: %s' % command)

#     if len(command) > 0:
#        bot.sendMessage(chat_id, teleBash(chat_id, command))
    


# #get key
# key = open('/opt/teleBot')
# bot = telepot.Bot(key.read().strip('\n'))
# key.close()
# bot.message_loop(handle)
# print('I am listening...')

# while 1:
#     try:
#         time.sleep(10)
    
#     except KeyboardInterrupt:
#         print('\n Program interrupted')
#         exit()
    
#     except:
#         print('Other error or exception occured!')
