import streamlit as st
import pandas as pd
from services.utils import add_school
from services.geopy import geocode_address
import uuid  # To generate unique IDs

# School Information Page
st.title("Enter School Information")

# Generate a unique School ID
unique_school_id = str(uuid.uuid4())  # Generates a unique UUID
st.write(f"Generated School ID: {unique_school_id}")

with st.form("school_form"):
    school_name = st.text_input("School Name")
    address = st.text_input("Address (Address or Coordinates)")
    
    # Adding more fields for detailed information
    school_start_time = st.time_input("School Start Time")
    school_end_time = st.time_input("School End Time")
    
    # Capacity and Disabilities
    total_students = st.number_input("Total Number of Students", min_value=1, step=1)
    disabilities_supported = st.multiselect("Types of Disabilities Supported", 
        ["Autism Spectrum Disorder", "Dyslexia", "Hearing Impairment", 
         "Visual Impairment", "Physical Disabilities", "Emotional Disturbance"])
    
    contact_person = st.text_input("Contact Person Name")
    contact_phone = st.text_input("Contact Phone Number")
    contact_email = st.text_input("Contact Email")
    
    # Additional details
    has_after_school_program = st.selectbox("Does the school have an after-school program?", ["Yes", "No"])
    after_school_program_details = st.text_area("After School Program Details (if applicable)")

    # Using the generated unique School ID
    school_id = unique_school_id
    school_submitted = st.form_submit_button("Submit")

    if school_submitted:
        
                # Geocode pickup and dropoff locations
        lat, lng = geocode_address(address)
        
        if lat and lng:
            add_school(school_name, address, school_start_time, school_end_time, total_students, 
                    disabilities_supported, contact_person, contact_phone, contact_email, 
                    has_after_school_program, after_school_program_details, school_id, lat, lng)
            st.success(f"School {school_name} added.")

# Display all schools in a table
st.subheader("School Information Table")
try:
    # Read the school data from CSV
    schools_df = pd.read_csv("./data/schools.csv")
    st.dataframe(schools_df)  # Display the school information as a table
except FileNotFoundError:
    st.error("No school data found. Please add a school first.")