# 
# json convert the python dictionary 
# above into a json
import json 
import turtle

# urllib.request fetch URLs using
# a variety of different protocols
import urllib.request 
import time 
 
# webbrowser provides a high-level interface
# to allow displaying Web-based documents 
# to users
import webbrowser 

# geocoder takes the data and locate these
# locations in the map
import geocoder
import math
lat = []
lon = []
iss_time = []

for i in range(2):

	# load the current status of the ISS in real-time
	url = "http://api.open-notify.org/iss-now.json"
	response = urllib.request.urlopen(url)
	result = json.loads(response.read())

	# Extract the ISS location
	location = result["iss_position"]
	lat.append(float(location['latitude']))
	lon.append(float(location['longitude']))
	iss_time.append(result["timestamp"])

	# Ouput lon and lat to the terminal
	print("\nLatitude: " + str(lat))
	print("\nLongitude: " + str(lon))
	print("\nTime: " + str(iss_time))

	# Refresh each 5 seconds
	time.sleep(5)

time_taken = iss_time[1] - iss_time[0]
lat_distance = lat[1] - lat[0]
lon_distance = lon[1] - lon[0]

distance1 = lat_distance*2*3.14*(6371000 + 400000)/360
distance2 = lon_distance*2*3.14*(6371000 + 400000)/360
'''
distance1 = lat_distance*2*3.14*(6371000)/360
distance2 = lon_distance*2*3.14*(6371000)/360
'''
print(lat_distance)
print(lon_distance)
print(distance1)
print(distance2)
total_distance = math.sqrt(distance1**2 + distance2**2)
print("speed is ", total_distance/time_taken)