# Python 3 program for the 
# haversine formula
import math
from time import sleep

from orbit import ISS

# Python 3 program for the
# haversine formula
def haversine(lat1, lon1, lat2, lon2):
	
	# distance between latitudes
	# and longitudes
	dLat = (lat2 - lat1) * math.pi / 180.0
	dLon = (lon2 - lon1) * math.pi / 180.0

	# convert to radians
	lat1 = (lat1) * math.pi / 180.0
	lat2 = (lat2) * math.pi / 180.0

	# apply formulae
	a = (pow(math.sin(dLat / 2), 2) +
		pow(math.sin(dLon / 2), 2) *
			math.cos(lat1) * math.cos(lat2));
	rad = 6371
	c = 2 * math.asin(math.sqrt(a))
	return rad * c



# This code is contributed 
# by ChitraNayal

def find_loc():
    location = ISS.coordinates() # Equivalent to ISS.at(timescale.now()).subpoint()
    print(location)

    print(f'Latitude: {location.latitude}')
    print(f'Longitude: {location.longitude}')
    print(f'Elevation: {location.elevation.km}')
    print(f'Lat: {location.latitude.degrees:.1f}, Long: {location.longitude.degrees:.1f}')
    #return f'Lat: {location.latitude.degrees:.1f}, Long: {location.longitude.degrees:.1f}'
    return location.latitude.degrees, location.longitude.degrees

# Driver code
'''
if __name__ == "__main__":
	lat1 = 51.5007
	lon1 = 0.1246
	lat2 = 40.6892
	lon2 = 74.0445
	
	print(haversine(lat1, lon1,lat2, lon2), "K.M.")
'''

lat1, long1 = find_loc()
p = [lat1, long1]
print("Point 1:",p)

sleep(5)

lat2, long2 = find_loc()
q = [lat2, long2]
print("Point 2:",q)

distance = haversine(lat1, long1,lat2, long2) # in km
distance = distance * 1000 # convert to m
speed = distance/5 # m/s
print("ISS speed:", speed, "m/s")
