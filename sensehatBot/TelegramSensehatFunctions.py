from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
sense.rotation = 180


def scrollIt(command):
    command.pop(0)
    listToStr = ' '.join(map(str, command))
    sense.show_message(listToStr, scroll_speed=0.05)
    sense.clear()


def getWeather(command):
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
    #'I don\'t know %s' % command
    print('in getWeather', switch.get(command))
    return switch.get(command)
