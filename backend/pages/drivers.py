import streamlit as st
import pandas as pd
from services.utils import add_driver
import uuid  # To generate unique IDs

# Bus Driver Information Page
st.title("Enter Bus Driver Information")
with st.form("driver_form"):
    driver_name = st.text_input("Driver Name")
    driver_license = st.text_input("License Number")
    driver_license_type = st.selectbox("License Type", ["Class A", "Class B", "Class C"])  # Example types
    driver_license_duration = st.number_input("License Duration (Years)", min_value=0, step=1)
    driver_insurance_status = st.selectbox("Insurance Status", ["Insured", "Not Insured"])
    driver_insurance_provider = st.text_input("Insurance Provider")
    driver_starting_location = st.text_input("Starting Location")
    driver_ending_location = st.text_input("Ending Location")
    driver_phone = st.text_input("Phone Number")
    driver_id = st.text_input("Driver ID")  # Unique identifier
    bus_id = st.text_input("Bus ID")  # Linking driver to bus
    driver_submitted = st.form_submit_button("Submit")

    if driver_submitted:
        add_driver(driver_name, driver_license, driver_license_type, driver_license_duration, driver_insurance_status, driver_insurance_provider, driver_starting_location, driver_ending_location, driver_phone, driver_id, bus_id)
        st.success(f"Bus Driver {driver_name} added.")

# Display all drivers in a table
st.subheader("Bus Driver Information Table")
try:
    # Read the driver data from CSV
    drivers_df = pd.read_csv("./data/drivers.csv")
    st.dataframe(drivers_df)  # Display the driver information as a table
except FileNotFoundError:
    st.error("No driver data found. Please add a driver first.")