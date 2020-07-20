from sense_hat import SenseHat
from random import random

sense = SenseHat()
sense.clear()
sense.rotation = 180


def listToString(list):
    listToStr = ' '.join(map(str, list))
    return listToStr


def scrollIt(command):
    command.pop(0)
    msg = listToString(command)
    sense.clear()
    sense.show_message(msg, scroll_speed=0.075)
    return 'message sent'


def getWeather(command):
    command.pop(0)
    t = round(sense.get_temperature_from_pressure(), 1)
    h = round(sense.get_humidity(), 1)
    p = round(sense.get_pressure(), 1)

    switch = {
        'temperature': f'The temperature is {t}',
        'humidity': f'The humidity is {h}',
        "pressure": f'The pressure is {p}',
        'report': "Temperature {temp}\nHumidity {humid}\nPressure {press}".format(
            temp=t, humid=h, press=p)
    }
    # 'I don\'t know %s' % command
    print('in getWeather', command)
    if (len(command) > 1 and command[0] == 'show'):
        dontKnow = 'I don\'t know {command}'.format(
            command=listToString(command))
        return scrollIt(['message', switch.get(command[1], dontKnow)])
    else:
        return switch.get(command, 'I don\'t know %s' % command)


def fiftyFifty():
    fifty = random()
    if (fifty > 0.4):
        return True
    else:
        return False


def noPhone():
    phone = fiftyFifty()
    if (phone):
        sense.set_pixels(allPixels([0, 255, 0]))
        return 'You can use your phone tonight'
    else:
        sense.set_pixels(allPixels([255, 0, 0]))
        return 'No phones tonight!'


def allPixels(color):
    return [color] * 64


print(allPixels([255, 0, 0]))
