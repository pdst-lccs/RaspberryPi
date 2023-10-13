# https://codeshare.io/r9ONgE

from datetime import datetime
from time import sleep
from sense_hat import SenseHat
import urllib3

sense = SenseHat()
pressure = sense.get_pressure()
temp = sense.get_temperature()
hum = sense.get_humidity()
time = datetime.now()
http = urllib3.PoolManager()

#ts1 = 'https://api.thingspeak.com/update?api_key=Z1BMZM118X2GG5H3&field1='
#ts2 = 'https://api.thingspeak.com/update?api_key=Z1BMZM118X2GG5H3&field2='

ts = 'https://api.thingspeak.com/update?api_key=DSRD8L1K92X1MAVT'

#for x in range(10):
while True:
    curtemp=str(sense.get_temperature())
    curhum=str(sense.get_humidity())
    curpress=str(sense.get_pressure())
    #http.request('GET',ts3+curtemp)
    #http.request('GET',ts2+curhum)
    http.request('GET',ts+'&field1='+curtemp+'&field2='+curhum+'&field3='+curpress)
    print(curtemp)
    #print(curhum)
    sleep(15)


print("end")