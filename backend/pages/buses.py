import streamlit as st
import pandas as pd
from services.utils import add_bus
import uuid  # To generate unique IDs

# Bus Information Page
st.title("Enter Bus Information")

# Generate a unique Bus ID
unique_bus_id = str(uuid.uuid4())  # Generates a unique UUID
st.write(f"Generated Bus ID: {unique_bus_id}")

# Create tabs for each bus type
tab_standard, tab_wheelchair = st.tabs(["Standard Bus", "Wheelchair Accessible Bus"])

# Standard Bus Tab
with tab_standard:
    st.subheader("Standard Bus Information")
    
    with st.form("standard_bus_form"):
        bus_capacity = st.selectbox("Select Number of Seats", [24, 30, 36])
        make = st.text_input("Make (e.g., Ford, Mercedes)")
        model = st.text_input("Model (e.g., Transit, Sprinter)")
        license_plate = st.text_input("License Plate")
        year_of_manufacture = st.number_input("Year of Manufacture", min_value=1900, max_value=2024, value=2024)
        fuel_type = st.selectbox("Fuel Type", ["Diesel", "Electric", "Hybrid", "Gasoline"])
        insurance_provider = st.text_input("Insurance Provider")
        insurance_policy_number = st.text_input("Insurance Policy Number")
        last_service_date = st.date_input("Last Service Date")
        notes = st.text_area("Additional Notes")

        # Using the generated unique Bus ID
        bus_id = unique_bus_id
        bus_submitted = st.form_submit_button("Submit")

        if bus_submitted:
            add_bus(bus_type="Standard", make=make, model=model, seat_count=bus_capacity, wheelchair_seats=0, 
                     license_plate=license_plate, year_of_manufacture=year_of_manufacture, 
                     fuel_type=fuel_type, insurance_provider=insurance_provider, 
                     insurance_policy_number=insurance_policy_number, last_service_date=last_service_date, 
                     notes=notes, bus_id=bus_id)
            st.success(f"Standard Bus {bus_id} added.")

# Wheelchair Accessible Bus Tab
with tab_wheelchair:
    st.subheader("Wheelchair Accessible Bus Information")
    
    with st.form("disability_bus_form"):
        bus_capacity = st.selectbox("Select Total Number of Seats", [15])  # Default for accessible bus
        wheelchair_seats = st.number_input("Number of Wheelchair Seats", min_value=1, max_value=3, value=1)

        make = st.text_input("Make (e.g., Ford, Mercedes)")
        model = st.text_input("Model (e.g., Transit, Sprinter)")
        license_plate = st.text_input("License Plate")
        year_of_manufacture = st.number_input("Year of Manufacture", min_value=1900, max_value=2024, value=2024)
        fuel_type = st.selectbox("Fuel Type", ["Diesel", "Electric", "Hybrid", "Gasoline"])
        insurance_provider = st.text_input("Insurance Provider")
        insurance_policy_number = st.text_input("Insurance Policy Number")
        last_service_date = st.date_input("Last Service Date")
        notes = st.text_area("Additional Notes")

        # Using the generated unique Bus ID
        bus_id = unique_bus_id
        bus_submitted = st.form_submit_button("Submit")

        if bus_submitted:
            add_bus(bus_type="Wheelchair Accessible", make=make, model=model, seat_count=bus_capacity, 
                     wheelchair_seats=wheelchair_seats, license_plate=license_plate, 
                     year_of_manufacture=year_of_manufacture, fuel_type=fuel_type, 
                     insurance_provider=insurance_provider, insurance_policy_number=insurance_policy_number, 
                     last_service_date=last_service_date, notes=notes, bus_id=bus_id)
            st.success(f"Wheelchair Accessible Bus {bus_id} added.")

# Display all buses in a table
st.subheader("Bus Information Table")
try:
    # Read the bus data from CSV
    buses_df = pd.read_csv("./data/buses.csv")
    st.dataframe(buses_df)  # Display the bus information as a table
except FileNotFoundError:
    st.error("No bus data found. Please add a bus first.")