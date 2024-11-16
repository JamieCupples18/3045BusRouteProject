import requests

# Replace 'YOUR_API_KEY' with your actual Geoapify API key
API_KEY = '80d85b89e8c44f638d8efb9e3730e30c'
API_URL = "https://api.geoapify.com/v1/geocode/search"

def geocode_address(address: str):
    params = {
        "text": address,
        "format": "json",
        "apiKey": API_KEY,
        "limit": 1  # Only get the first result
    }
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        # Check if results are returned
        if data.get("results"):
            # Extract latitude and longitude from the first result
            lat = data["results"][0].get("lat")
            lon = data["results"][0].get("lon")
            return lat, lon
        else:
            print(f"No results found for address: {address}")
            return None, None
    else:
        print(f"Error in API request: {response.status_code}")
        return None, None