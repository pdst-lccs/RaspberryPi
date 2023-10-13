from sense_hat import SenseHat
from time import sleep
from random import randint
from random import choice
#import random

sense = SenseHat()
sense.clear()
# RGB colour system
red = (255, 0, 0)     # red
green = (0, 255, 0)     # red
blue = (0, 0, 225)
blank = (0, 0, 0)
colours = [red, green, blue]

for i in range(634):
    x = randint(0, 7)
    print(x)

    y = randint(0, 7)
    print(y)
    
    sleep(0.1)

    colour = choice(colours)
    sense.set_pixel(x, y, colour)



'''
for i in range(10):
    x = randint(0, 7)
    print(x)

    y = randint(0, 7)
    print(y)

    sleep(0.5)

    sense.set_pixel(x, y, green)
'''