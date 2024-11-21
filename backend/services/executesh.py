import subprocess
import csv
import json
import os

def load_csv_data(filename):
    """Load data from a CSV file and return a list of dictionaries."""
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def execute_curl_command():
    # Load school and student data from CSV files
    schools = load_csv_data('../backend/data/schools.csv')
    students = load_csv_data('../backend/data/students.csv')  

    # Prepare the list of locations
    locations = []

    # Add the school location
    for school in schools:
        locations.append({
            "address": school['address'],  # Ensure the CSV has the correct field names
            "lat": school['lat'],
            "lng": school['lng']
        })
        school_location = {
            "address": school['address'],
            "lat": school['lat'],
            "lng": school['lng']
        }  # Store the school location to reuse it as the finish location

    # Add the student locations
    for student in students:
        locations.append({
            "address": student['address'],  # Ensure the CSV has the correct field names
            "lat": student['lat'],
            "lng": student['lng']
        })

    # Reuse the school location as the finish location by appending it to the list again
    locations.append({
        "address": school_location['address'],
        "lat": school_location['lat'],
        "lng": school_location['lng']
    })

    # Convert locations list to the required JSON format for curl
    locations_json = str(locations).replace("'", '"')  # Convert single quotes to double quotes for valid JSON

    # Define the curl command with dynamic locations
    curl_command = f"""
    curl \
    --url https://api.routexl.com/tour/ \
    --user jnah:3045 \
    --data 'locations={locations_json}'
    """

    print("Executing the following curl command:")
    print(curl_command)  # Print the full curl command for clarity
    
    # Run the curl command using subprocess and capture both stdout and stderr
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

    # Check the result of the command execution
    if result.returncode == 0:
        print("Command executed successfully.")
        response = result.stdout  # Capture the curl output (response from RouteXL API)
        print("Raw Response:", response)  # Print the raw response for debugging

        # Save the response to a JSON file
        try:
            response_json = json.loads(response)  # Try to parse the response as JSON
            output_file = '../backend/data/response.json'
            os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Ensure the directory exists
            with open(output_file, 'w') as json_file:
                json.dump(response_json, json_file, indent=4)  # Save the JSON response to a file
            print(f"Response saved to '{output_file}'")
        except json.JSONDecodeError:
            print("Error: The response is not a valid JSON format.")
            print(f"Raw response: {response}")  # Show the raw response
    else:
        print("Command failed with error:")
        print(result.stderr)  # Print any error that occurred during the execution

# Call the function to execute the curl command
execute_curl_command()