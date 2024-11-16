import streamlit as st
import pandas as pd
from services.utils import add_student
from services.geopy import geocode_address  # Ensure geocode_address is imported
import uuid  # To generate unique IDs

# Student Information Page
st.title("Enter Student Information")

# Generate a unique Student ID
unique_student_id = str(uuid.uuid4())  # Generates a unique UUID
st.write(f"Generated Student ID: {unique_student_id}")

with st.form("student_form"):
    # Basic Student Details
    student_name = st.text_input("Student Name")
    student_age = st.number_input("Student Age", min_value=1, step=1)
    student_grade = st.text_input("Grade/Year")
    address = st.text_input("Location (Address or Coordinates)")
    student_needs = st.multiselect("Special Needs", ["Wheelchair", "Assistant", "Other"])
    primary_language = st.text_input("Primary Language")

    # Related School Information
    school_id = st.text_input("School ID")
    school_name = st.text_input("School Name (if known)")

    # Transportation Details
    preferred_pickup_time = st.time_input("Preferred Pickup Time")
    preferred_dropoff_time = st.time_input("Preferred Dropoff Time")

    # Parent/Guardian Information
    parent_1_name = st.text_input("Parent/Guardian 1 Name")
    parent_1_phone = st.text_input("Parent/Guardian 1 Phone Number")
    parent_1_email = st.text_input("Parent/Guardian 1 Email")
    
    parent_2_name = st.text_input("Parent/Guardian 2 Name (Optional)")
    parent_2_phone = st.text_input("Parent/Guardian 2 Phone Number (Optional)")
    parent_2_email = st.text_input("Parent/Guardian 2 Email (Optional)")

    # Emergency Contact Details
    emergency_contact_name = st.text_input("Emergency Contact Name")
    emergency_contact_relationship = st.text_input("Relationship to Student")
    emergency_contact_phone = st.text_input("Emergency Contact Phone Number")

    # Additional Notes
    additional_notes = st.text_area("Additional Notes or Special Instructions")
    
    # Using the generated unique Student ID
    student_id = unique_student_id
    student_submitted = st.form_submit_button("Submit")

    if student_submitted:
        # Geocode pickup and dropoff locations
        lat, lng = geocode_address(address)

        
        if lat and lng:
            # Now, call the add_student function with the latitudes and longitudes
            add_student(student_id, student_name, student_age, student_grade, address, student_needs, 
                        primary_language, school_id, school_name, preferred_pickup_time, preferred_dropoff_time, parent_1_name, parent_1_phone, 
                        parent_1_email, parent_2_name, parent_2_phone, parent_2_email, emergency_contact_name, 
                        emergency_contact_relationship, emergency_contact_phone, additional_notes, 
                        lat, lng)
            st.success(f"Student {student_name} added.")
        else:
            st.error("Could not geocode one or more of the addresses. Please check the address format.")
            
            
# Display all students in a table
st.subheader("Student Information Table")
try:
    # Read the student data from CSV
    students_df = pd.read_csv("./data/students.csv")
    st.dataframe(students_df)  # Display the student information as a table
except FileNotFoundError:
    st.error("No student data found. Please add a student first.")