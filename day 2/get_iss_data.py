import requests

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

# Function to display ISS data
def display_iss_data(iss_data):
    if iss_data:
        latitude = iss_data["iss_position"]["latitude"]
        longitude = iss_data["iss_position"]["longitude"]
        timestamp = iss_data["timestamp"]

        print(f"ISS Data (Timestamp: {timestamp}):")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    else:
        print("No ISS data to display.")

if __name__ == "__main__":
    iss_data = fetch_iss_data()
    display_iss_data(iss_data)
