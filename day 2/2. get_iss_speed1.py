from time import sleep
import math
from orbit import ISS


def find_loc():
    location = ISS.coordinates() # Equivalent to ISS.at(timescale.now()).subpoint()
    print(location)

    print(f'Latitude: {location.latitude}')
    print(f'Longitude: {location.longitude}')
    print(f'Elevation: {location.elevation.km}')
    print(f'Lat: {location.latitude.degrees:.1f}, Long: {location.longitude.degrees:.1f}')
    #return f'Lat: {location.latitude.degrees:.1f}, Long: {location.longitude.degrees:.1f}'
    return location.latitude.degrees, location.longitude.degrees


lat1, long1 = find_loc()
p = [lat1, long1]
print("Point 1:",p)

sleep(5)

lat2, long2 = find_loc()
q = [lat2, long2]
print("Point 2:",q)

# Calculate Euclidean distance between 2 points
#print (math.dist(p, q))
distance = math.sqrt( ((p[0]-q[0])**2)+((p[1]-q[1])**2) )
print(distance)
speed = distance/5
print(speed)



