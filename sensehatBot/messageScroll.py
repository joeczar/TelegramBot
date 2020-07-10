from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
sense.rotation = 180


def scrollIt(command):
    command.pop(0)
    listToStr = ' '.join(map(str, command))
    sense.show_message(listToStr, scroll_speed=0.05)
