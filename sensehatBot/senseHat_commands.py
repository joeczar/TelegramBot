from TelegramSensehatFunctions import getWeather, scrollIt


def handleCommands(command):
    command = command.lower().split()

    if command[0] == 'weather':
        return getWeather(command)
    elif command[0] == 'message':
        return scrollIt(command)
    else:
        listToStr = ' '.join(map(str, command))
        return 'I didn\'t understand %s' % listToStr
