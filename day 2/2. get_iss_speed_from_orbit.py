import math

# Constants
earth_radius = 6371  # Earth's radius in kilometers (mean value)
orbital_altitude = 420  # Altitude of the ISS in kilometers
orbital_period = 90.39  # Orbital period of the ISS in minutes

# Convert orbital period from minutes to seconds
orbital_period_seconds = orbital_period * 60

# Calculate the speed of the ISS
speed = (2 * math.pi * (earth_radius + orbital_altitude) * 1000) / orbital_period_seconds  # Speed in meters per second

print(f"The speed of the ISS is approximately {speed:.2f} meters per second")
