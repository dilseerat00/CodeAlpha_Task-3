import http.client
import json
import webbrowser

# Function to get geolocation based on IP address
def get_geolocation(ip_address=''):
    try:
        conn = http.client.HTTPConnection('ip-api.com')
        if ip_address:
            conn.request('GET', f'/json/{ip_address}')
        else:
            conn.request('GET', '/json/')
        response = conn.getresponse()
        data = response.read()
        conn.close()
        geolocation = json.loads(data.decode('utf-8'))
        if geolocation['status'] == 'fail':
            print(f"Failed to get geolocation: {geolocation['message']}")
            return None
        return geolocation
    except Exception as e:
        print(f"Error fetching geolocation: {e}")
        return None

# Function to display location details
def show_location():
    geolocation = get_geolocation()
    if geolocation:
        latitude = geolocation['lat']
        longitude = geolocation['lon']
        city = geolocation['city']
        country = geolocation['country']
        print(f"Latitude: {latitude}, Longitude: {longitude}")
        print(f"City: {city}, Country: {country}")

# Function to update and show location
def update_location():
    show_location()

# Function to open the map in a browser
def open_map_in_browser():
    geolocation = get_geolocation()
    if geolocation:
        latitude = geolocation['lat']
        longitude = geolocation['lon']
        map_url = f"https://www.openstreetmap.org/?mlat={latitude}&mlon={longitude}&zoom=12"
        print(f"Opening map at: {map_url}")
        webbrowser.open(map_url)

# Main function to handle menu options
def main():
    while True:
        print("\nMenu:")
        print("1. Show My Location")
        print("2. Update Location")
        print("3. Open Map in Browser")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_location()
        elif choice == '2':
            update_location()
        elif choice == '3':
            open_map_in_browser()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()
