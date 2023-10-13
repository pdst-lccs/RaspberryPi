"""
This program uploads Raspberry Pi temperature data to ThingSpeak every 20 seconds.
1. Get this program to run correctly
2. Try it with your own Thingspeak Channel
3. On a Raspberry Pi, try streaming the current CPU Temperature. You can find this code here:
https://raw.githubusercontent.com/STJRush/handycode/master/ALT4%20Sensors%20Inputs%20Outputs/Raspberry%20PI%20Sensors/CPU_Temperature_Measure_Simple.py

On the free version of ThingSpeak you can only send data every 15 seconds.

"""


import sys 
from time import sleep 
from urllib.request import urlopen
from sense_hat import SenseHat


sense = SenseHat()

api_key = "S51IWS802ZPXAR4N"  #your WRITE key from your own thingspeak account. Put yours here.

def update_ThingSpeak(): 
   print('Now updating thingspeak') 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % api_key    

   f = urlopen(baseURL + "&field1=%s" %t)
   print ("Success! I uploaded data point No. ", f.read())
   f.close()

# Program Starts Here
while True:
    t1 = sense.get_temperature()
    t2 = sense.get_temperature_from_pressure()
    t = round((t1+t2)/2, 1)
    print("Temperature:", t)

    update_ThingSpeak()
    
    print("Now waiting another 20 seconds before uploading more data to thingspeak...") 
    sleep(20)
    print("")



