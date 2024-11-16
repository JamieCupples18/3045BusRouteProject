import pandas as pd
from datetime import datetime

# File paths for CSV files
STUDENTS_CSV = "./data/students.csv"
SCHOOLS_CSV = "./data/schools.csv"
DRIVERS_CSV = "./data/drivers.csv"
BUSES_CSV = "./data/buses.csv"

# Function to create initial CSV files with headers if they don't exist
def create_initial_csv(file_name, headers):
    try:
        pd.read_csv(file_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=headers)
        df.to_csv(file_name, index=False)

# Function to add a student
def add_student(student_id, name, age, grade, address, needs, primary_language, school_id, 
                school_name, pickup_time, dropoff_time, parent_1_name, parent_1_phone, parent_1_email, parent_2_name, parent_2_phone, 
                parent_2_email, emergency_contact_name, emergency_contact_relationship, 
                emergency_contact_phone, additional_notes, lat, lng):

    
    create_initial_csv(STUDENTS_CSV, [
        "student_id", "name", "age", "grade", "address", "needs", "primary_language",
        "school_id", "school_name", "preferred_pickup_time", "preferred_dropoff_time", "parent_1_name", "parent_1_phone", 
        "parent_1_email", "parent_2_name", "parent_2_phone", "parent_2_email",
        "emergency_contact_name", "emergency_contact_relationship", "emergency_contact_phone",
        "additional_notes", "lat", "lng"
    ])
    
    students_df = pd.read_csv(STUDENTS_CSV)
    new_student = pd.DataFrame({
        "student_id": [student_id],
        "name": [name],
        "age": [age],
        "grade": [grade],
        "address": [address],
        "needs": [", ".join(needs)],
        "primary_language": [primary_language],
        "school_id": [school_id],
        "school_name": [school_name],
        "preferred_pickup_time": [pickup_time],
        "preferred_dropoff_time": [dropoff_time],
        "parent_1_name": [parent_1_name],
        "parent_1_phone": [parent_1_phone],
        "parent_1_email": [parent_1_email],
        "parent_2_name": [parent_2_name],
        "parent_2_phone": [parent_2_phone],
        "parent_2_email": [parent_2_email],
        "emergency_contact_name": [emergency_contact_name],
        "emergency_contact_relationship": [emergency_contact_relationship],
        "emergency_contact_phone": [emergency_contact_phone],
        "additional_notes": [additional_notes],
        "lat": [lat],
        "lng": [lng],

    })
    updated_df = pd.concat([students_df, new_student], ignore_index=True)
    updated_df.to_csv(STUDENTS_CSV, index=False)

# Function to add a school
def add_school(school_name, address, start_time, end_time, total_students, disabilities_supported, 
               contact_person, contact_phone, contact_email, after_school_program, 
               after_school_program_details, school_id, lat, lng):
    
    create_initial_csv(SCHOOLS_CSV, [
        "school_id", "school_name", "address", "start_time", "end_time", 
        "total_students", "disabilities_supported", "contact_person", 
        "contact_phone", "contact_email", "after_school_program", 
        "after_school_program_details", "lat", "lng"
    ])
    
    schools_df = pd.read_csv(SCHOOLS_CSV)
    new_school = pd.DataFrame({
        "school_id": [school_id],
        "school_name": [school_name],
        "address": [address],
        "start_time": [start_time],
        "end_time": [end_time],
        "total_students": [total_students],
        "disabilities_supported": [", ".join(disabilities_supported)],
        "contact_person": [contact_person],
        "contact_phone": [contact_phone],
        "contact_email": [contact_email],
        "after_school_program": [after_school_program],
        "after_school_program_details": [after_school_program_details],
        "lat": [lat],
        "lng": [lng]
    })
    updated_df = pd.concat([schools_df, new_school], ignore_index=True)
    updated_df.to_csv(SCHOOLS_CSV, index=False)

# Function to add a driver
def add_driver(name, license_number, license_type, license_duration, insurance_status, insurance_provider, starting_location, ending_location, phone, driver_id, bus_id):
    
    create_initial_csv(DRIVERS_CSV, [
        "id", "name", "license", "license_type", "license_duration", 
        "insurance_status", "insurance_provider", "starting_location", 
        "ending_location", "phone", "bus_id"
    ])
    
    drivers_df = pd.read_csv(DRIVERS_CSV)
    new_driver = pd.DataFrame({
        "id": [driver_id],
        "name": [name],
        "license": [license_number],
        "license_type": [license_type],
        "license_duration": [license_duration],
        "insurance_status": [insurance_status],
        "insurance_provider": [insurance_provider],
        "starting_location": [starting_location],
        "ending_location": [ending_location],
        "phone": [phone],
        "bus_id": [bus_id]
    })
    updated_df = pd.concat([drivers_df, new_driver], ignore_index=True)
    updated_df.to_csv(DRIVERS_CSV, index=False)

# Function to add a bus
def add_bus(bus_type, make, model, seat_count, wheelchair_seats, license_plate, year_of_manufacture, fuel_type, insurance_provider, insurance_policy_number, last_service_date, notes, bus_id):
    
    create_initial_csv(BUSES_CSV, [
        "bus_id", "bus_type", "make", "model", "seat_count", "wheelchair_seats", 
        "license_plate", "year_of_manufacture", "fuel_type", "insurance_provider", 
        "insurance_policy_number", "last_service_date", "notes"
    ])
    
    buses_df = pd.read_csv(BUSES_CSV)
    new_bus = pd.DataFrame({
        "bus_id": [bus_id],
        "bus_type": [bus_type],
        "make": [make],
        "model": [model],
        "seat_count": [seat_count],
        "wheelchair_seats": [wheelchair_seats if bus_type == "Wheelchair Accessible" else 0],
        "license_plate": [license_plate],
        "year_of_manufacture": [year_of_manufacture],
        "fuel_type": [fuel_type],
        "insurance_provider": [insurance_provider],
        "insurance_policy_number": [insurance_policy_number],
        "last_service_date": [last_service_date.strftime("%Y-%m-%d") if isinstance(last_service_date, datetime) else last_service_date],
        "notes": [notes]
    })
    updated_df = pd.concat([buses_df, new_bus], ignore_index=True)
    updated_df.to_csv(BUSES_CSV, index=False)