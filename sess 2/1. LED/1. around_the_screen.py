from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

r = (255, 0, 0)     # red
o = (255, 128, 0)   # orange
y = (255, 255, 0)   # yellow
g = (0, 255, 0)     # green
c = (0, 255, 255)   # cyan
b = (0, 0, 255)     # blue
p = (255, 0, 255)   # purple
n = (255, 128, 128) # pink
w =(255, 255, 255)  # white
k = (0, 0, 0)       # blank

rainbow = [r, o, y, g, c, b, p, n]

sense.clear()

# down in col 0 (x=0)
for y in range(8):
    sense.set_pixel(0, y, r)
    sleep(0.5)

# across in row 7 (y=7)
for x in range(1, 8):
    sense.set_pixel(x, 7, r)
    sleep(0.5)

# up in col 7 (x=7)
for y in range(7, -1, -1):
    sense.set_pixel(7, y, b)
    sleep(0.5)



'''
# Draw a diagonal using the colours of the rainbow
y = 0
x = 0
for colour in rainbow:
    sense.set_pixel(x, y, colour)
    x+=1
    y+=1
    sleep(1)
'''
