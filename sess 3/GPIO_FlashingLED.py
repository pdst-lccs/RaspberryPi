from gpiozero import LED
from time import sleep

led = LED(25) #let GPIO Zero know which GPIO pin the LED is connected to
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
