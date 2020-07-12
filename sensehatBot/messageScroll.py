from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
sense.rotation = 180


def scrollIt(command):
    command.pop(0)
    listToStr = ' '.join(map(str, command))
    sense.show_message(listToStr, scroll_speed=0.05, back_colour=[
                       0, 0, 255], text_colour=[255, 0, 0])


msg = 'message eat a dick'.split(' ')
scrollIt(msg)
sense.clear()
