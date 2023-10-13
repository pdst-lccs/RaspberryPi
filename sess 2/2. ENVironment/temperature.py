#from sense_emu import SenseHat
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

green = (0, 255, 0)
red = (255, 0, 0)

t = sense.get_temperature()
t = round(t, 1)
print(t)

while True:
    # 18.3 and 26.7
    t = sense.get_temperature()
    t = round(t, 1)
    if t > 18.3 and t < 26.7:
        sense.show_message(str(t), back_colour=green)
    else:
        sense.show_message(str(t), back_colour=red)
