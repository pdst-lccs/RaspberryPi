# exif
from exif import Image
from datetime import datetime
import math

def get_time(image):
    with open(image, 'rb') as image_file:
        img = Image(image_file)
        #for data in img.list_all():
        #    print(data)
        time_str = img.get("datetime_original")
        #print("time_str", time_str)
        time = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
        #print("time", time)
        return time

def get_time_difference(image_1, image_2):
    time_1 = get_time(image_1)
    time_2 = get_time(image_2)
    time_difference = time_2 - time_1
    return time_difference.seconds

# https://gis.stackexchange.com/questions/379093/identifying-coordinate-format-from-exif-data
def dms_to_dd(gps_coords, gps_coords_ref):
    d, m, s =  gps_coords
    dd = d + m / 60 + s / 3600
    #if gps_coords_ref.upper() in ('S', 'W'):
    #    return -dd
    #elif gps_coords_ref.upper() in ('N', 'E'):
    #    return dd
    #else:
    #    raise RuntimeError('Incorrect gps_coords_ref {}'.format(gps_coords_ref))
    return dd

def get_location(image):
    with open(image, 'rb') as image_file:
        img = Image(image_file)
        #for data in img.list_all():
        #    print(data)
        dms_lat = img.get("gps_latitude") # JE: I think this is deg, mins and secs
        dd_lat = dms_to_dd(dms_lat, None) # TODO: pass in the ref
        #print(dd_lat)
        
        dms_lon = img.get("gps_longitude")
        dd_lon = dms_to_dd(dms_lon, None)
        #print(dd_lon)
        
        return dd_lat, dd_lon
        
def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c # JE: I may need to add ISS altitude here

    return distance

lat1, lon1 = get_location('imgs_from_iss\\photo_1744.jpg')
lat2, lon2 = get_location('imgs_from_iss\\photo_1745.jpg')
dist = haversine(lat1, lon1, lat2, lon2)
dist *= 1000 #convert to metres
print(dist)

# JE: To do ... loop through adjacent pics between photo_1744 and photo_1761 and smooth out all the speeds


# Calculate the distance
#dist = haversine(lat1, lon1, lat2, lon2)
#print(f"The distance between the two points is {dist:.2f} km")


td = get_time_difference('imgs_from_iss\\photo_1754.jpg', 'imgs_from_iss\\photo_1755.jpg')
print(td)

print("Speed:", dist/td, "m/s")
