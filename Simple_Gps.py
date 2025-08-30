from geopy import Nominatim
from geopy.distance import great_circle

def Calculate_distance(start_address, end_address):

    geolocator = Nominatim(user_agent="simplegps-app")

    try:
        print(f"Finding Coordinates for : {start_address}...")
        start_location = geolocator.geocode(start_address)
        if not start_location:
            print(f"Could not find coordinates for : {end_address}")
            return None

        print(f"Finding coordinates for : {end_address}....")
        end_location = geolocator.geocode(end_address)
        if not end_location:
            print(f"Could not find coordinates for : {end_address}")
            return None

        start_coords = (start_location.latitude, start_location.longitude)
        end_coords = (end_location.latitude, end_location.longitude)

        distance_km = great_circle(start_coords, end_coords).km

        return start_coords, end_coords, distance_km

    except Exception as e:
        print(f"An error occured : {e}")
        return None


if __name__ == "__main__":
    start_point = input("Enter the starting address : ")
    end_point= input("Enter the destination address : ")

    result = Calculate_distance(start_point, end_point)

    if result:
        start_coords, end_coords, distance = result
        print("|n----GPS Report----")
        print(f"Starting coodinates : {start_coords}")
        print(f"Destination coordinates: {end_coords}")
        print(f"Distance : {distance : 2f} km")

    else:
        print("|n Distance calculation Failed. Please check your address and try again")
