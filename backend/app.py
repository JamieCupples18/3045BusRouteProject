import os
import json
import streamlit as st
import pandas as pd
from services.executesh import execute_curl_command


# Function to load and format data from the response JSON file
def load_and_format_data():
    # Get base directory to ensure correct pathing
    base_dir = os.path.dirname(__file__)  # Get the directory of this script
    response_file_path = os.path.join(base_dir, 'data', 'response.json')

    # Check if the response file exists
    if not os.path.exists(response_file_path):
        st.error(f"Response file missing at: {response_file_path}. Please execute the curl command.")
        return None

    # Check if response file is empty
    if os.path.getsize(response_file_path) == 0:
        st.error("Response file is empty. Please check the API response.")
        return None

    # Load JSON data
    try:
        with open(response_file_path, 'r') as res_file:
            response_data = json.load(res_file)
    except Exception as e:
        st.error(f"Error loading JSON file: {e}")
        return None

    # Validate required keys in JSON data
    if "route" not in response_data:
        st.error("Invalid data format: Missing 'route' key in response file.")
        return None

    # Extract route information from the response
    formatted_data = []
    for i, (key, route_info) in enumerate(response_data["route"].items()):
        formatted_entry = {
            "Stop #": i + 1,
            "Address": route_info.get("name", "N/A"),
            "Arrival Time": route_info.get("arrival", "N/A"),
            "Distance (km)": route_info.get("distance", "N/A"),
        }
        formatted_data.append(formatted_entry)

    # Convert to DataFrame for display
    return pd.DataFrame(formatted_data)



# Streamlit app
def streamlit_app():
    st.title("Optimized Bus Route Planner")

    # Button to execute the curl command
    if st.button("Execute Curl Command"):
        st.info("Executing curl command...")
        try:
            execute_curl_command()
            st.success("Curl command executed successfully. Files generated.")
        except Exception as e:
            st.error(f"Error executing curl command: {e}")

    # Button to display route details
    if st.button("Display Route Details"):
        formatted_data = load_and_format_data()
        if formatted_data is not None and not formatted_data.empty:
            st.subheader("Route Details")
            st.write("Here is a summary of the optimized route:")
            st.table(formatted_data)
        else:
            st.warning("No route details available to display.")



# Run the Streamlit app
if __name__ == "__main__":
    streamlit_app()