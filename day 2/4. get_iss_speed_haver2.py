import requests
import time
from math import radians, sin, cos, sqrt

# Function to fetch ISS data
def fetch_iss_data():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        response.raise_for_status()  # Check for HTTP errors

        iss_data = response.json()
        return iss_data

    except requests.exceptions.RequestException as e:
        print("Error: Unable to fetch ISS data.")
        print(e)
        return None

# Function to calculate haversine distance between two points on the Earth's surface
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * sqrt(a)
    distance = 6371 * c  # Earth's radius in kilometers
    return distance

if __name__ == "__main__":
    prev_iss_data = fetch_iss_data()
    
    while True:
        time.sleep(5)  # Wait for a few seconds
        current_iss_data = fetch_iss_data()

        if prev_iss_data and current_iss_data:
            # Calculate time elapsed
            time1 = prev_iss_data["timestamp"]
            time2 = current_iss_data["timestamp"]
            time_elapsed = (time2 - time1)  # Time in seconds

            # Calculate haversine distance between the two data points
            lat1 = float(prev_iss_data["iss_position"]["latitude"])
            lon1 = float(prev_iss_data["iss_position"]["longitude"])
            lat2 = float(current_iss_data["iss_position"]["latitude"])
            lon2 = float(current_iss_data["iss_position"]["longitude"])
            distance = haversine(lat1, lon1, lat2, lon2)  # Distance in kilometers

            # Calculate speed
            speed = distance / (time_elapsed / 3600)  # Speed in kilometers per hour
            mps_speed = 0.277778 * speed

            print(f"ISS Speed: {speed:.2f} km/h which is {mps_speed:.2f} mp/s")

        prev_iss_data = current_iss_data
