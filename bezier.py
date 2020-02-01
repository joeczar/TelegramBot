import math
import time
from blinkt import set_brightness, set_all, set_pixel, show, clear

def bezierFade(start, end, steps):
    # increment or decrement by ten steps
    # get the difference between start & end
    diff = end - start
    # calculate value of each step
    interval = diff / steps
    #set val to start value
    val = start
    for step in range(steps):
        bez = ((1 + math.cos(math.pi + val * math.pi)) / 2)
        val += interval
        if start < end:
            beziOut = bez + start
        else:
            beziOut = bez
        set_brightness(beziOut)
        show()
        
# clear the LEDs
bright = 0.1
set_brightness(bright)
clear()
set_all(255, 0, 0)
show()
time.sleep(1)

beziInOut(0, 0.5, 10)
time.sleep(1)
beziInOut(0.5, 0, 10)
time.sleep(1)


