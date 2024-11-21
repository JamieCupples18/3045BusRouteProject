import pytest
from unittest.mock import patch
from ..services.geopy import geocode_address  # Replace with the actual import path

# Mock API response
MOCK_API_RESPONSE = {
    "results": [
        {
            "lat": 40.7128,
            "lon": -74.0060
        }
    ]
}

# Test case to mock the API request and test geocode_address
def test_geocode_address_success():
    with patch('requests.get') as mock_get:
        # Mock the GET request to return a predefined response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = MOCK_API_RESPONSE
        
        address = "New York, USA"
        lat, lon = geocode_address(address)
        
        assert lat == 40.7128
        assert lon == -74.0060
        mock_get.assert_called_once_with(
            "https://api.geoapify.com/v1/geocode/search",
            params={
                "text": address,
                "format": "json",
                "apiKey": "80d85b89e8c44f638d8efb9e3730e30c",
                "limit": 1
            }
        )

def test_geocode_address_no_results():
    with patch('requests.get') as mock_get:
        # Mock the GET request to return a response with no results
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"results": []}
        
        address = "Nonexistent Address"
        lat, lon = geocode_address(address)
        
        assert lat is None
        assert lon is None
        mock_get.assert_called_once_with(
            "https://api.geoapify.com/v1/geocode/search",
            params={
                "text": address,
                "format": "json",
                "apiKey": "80d85b89e8c44f638d8efb9e3730e30c",
                "limit": 1
            }
        )

def test_geocode_address_api_error():
    with patch('requests.get') as mock_get:
        # Mock the GET request to return an error status code
        mock_get.return_value.status_code = 500
        
        address = "New York, USA"
        lat, lon = geocode_address(address)
        
        assert lat is None
        assert lon is None
        mock_get.assert_called_once_with(
            "https://api.geoapify.com/v1/geocode/search",
            params={
                "text": address,
                "format": "json",
                "apiKey": "80d85b89e8c44f638d8efb9e3730e30c",
                "limit": 1
            }
        )