import pytest
import pandas as pd
import os
from datetime import datetime
from unittest.mock import patch
from backend.services.utils import add_student, add_school, add_driver, add_bus, create_initial_csv

# Mock file paths for testing
TEST_STUDENTS_CSV = "./test_data/students.csv"
TEST_SCHOOLS_CSV = "./test_data/schools.csv"
TEST_DRIVERS_CSV = "./test_data/drivers.csv"
TEST_BUSES_CSV = "./test_data/buses.csv"

@pytest.fixture
def setup_test_files():
    # Ensure test directory exists
    os.makedirs("./test_data", exist_ok=True)
    yield
    # Clean up after tests
    for file in [TEST_STUDENTS_CSV, TEST_SCHOOLS_CSV, TEST_DRIVERS_CSV, TEST_BUSES_CSV]:
        if os.path.exists(file):
            os.remove(file)
    os.rmdir("./test_data")

@patch("backend.services.utils.STUDENTS_CSV", TEST_STUDENTS_CSV)
@patch("backend.services.utils.SCHOOLS_CSV", TEST_SCHOOLS_CSV)
@patch("backend.services.utils.DRIVERS_CSV", TEST_DRIVERS_CSV)
@patch("backend.services.utils.BUSES_CSV", TEST_BUSES_CSV)

@pytest.mark.filterwarnings("ignore::FutureWarning")
def test_add_student(setup_test_files):
    add_student(
        student_id="S001", name="Alice", age=10, grade="5th", address="123 Elm St",
        needs=["Hearing Aid"], primary_language="English", school_id="SCH001", school_name="Greenwood High",
        pickup_time="08:00 AM", dropoff_time="03:00 PM", parent_1_name="John Doe",
        parent_1_phone="1234567890", parent_1_email="john.doe@example.com", parent_2_name="Jane Doe",
        parent_2_phone="0987654321", parent_2_email="jane.doe@example.com", emergency_contact_name="Bob Smith",
        emergency_contact_relationship="Uncle", emergency_contact_phone="1112223333", additional_notes="Allergic to nuts",
        lat=40.7128, lng=-74.0060
    )
    df = pd.read_csv(TEST_STUDENTS_CSV)
    assert len(df) == 1
    assert df.loc[0, "name"] == "Alice"

@patch("backend.services.utils.STUDENTS_CSV", TEST_STUDENTS_CSV)
@patch("backend.services.utils.SCHOOLS_CSV", TEST_SCHOOLS_CSV)
@patch("backend.services.utils.DRIVERS_CSV", TEST_DRIVERS_CSV)
@patch("backend.services.utils.BUSES_CSV", TEST_BUSES_CSV)

@pytest.mark.filterwarnings("ignore::FutureWarning")
def test_add_school(setup_test_files):
    add_school(
        school_name="Greenwood High", address="456 Oak St", start_time="08:30 AM",
        end_time="03:30 PM", total_students=500, disabilities_supported=["Visual Impairment"],
        contact_person="Ms. Green", contact_phone="555-1234", contact_email="greenwood@school.com",
        after_school_program=True, after_school_program_details="Sports and Arts", school_id="SCH001",
        lat=40.7128, lng=-74.0060
    )
    df = pd.read_csv(TEST_SCHOOLS_CSV)
    assert len(df) == 1
    assert df.loc[0, "school_name"] == "Greenwood High"

@patch("backend.services.utils.STUDENTS_CSV", TEST_STUDENTS_CSV)
@patch("backend.services.utils.SCHOOLS_CSV", TEST_SCHOOLS_CSV)
@patch("backend.services.utils.DRIVERS_CSV", TEST_DRIVERS_CSV)
@patch("backend.services.utils.BUSES_CSV", TEST_BUSES_CSV)

@pytest.mark.filterwarnings("ignore::FutureWarning")
def test_add_driver(setup_test_files):
    add_driver(
        name="Tom", license_number="L12345", license_type="Class B", license_duration=5,
        insurance_status="Valid", insurance_provider="State Farm", starting_location="Garage A",
        ending_location="Garage B", phone="555-6789", driver_id="D001", bus_id="B001"
    )
    df = pd.read_csv(TEST_DRIVERS_CSV)
    assert len(df) == 1
    assert df.loc[0, "name"] == "Tom"

@patch("backend.services.utils.STUDENTS_CSV", TEST_STUDENTS_CSV)
@patch("backend.services.utils.SCHOOLS_CSV", TEST_SCHOOLS_CSV)
@patch("backend.services.utils.DRIVERS_CSV", TEST_DRIVERS_CSV)
@patch("backend.services.utils.BUSES_CSV", TEST_BUSES_CSV)

@pytest.mark.filterwarnings("ignore::FutureWarning")
def test_add_bus(setup_test_files):
    add_bus(
        bus_type="Standard", make="Ford", model="Transit", seat_count=40, wheelchair_seats=0,
        license_plate="ABC123", year_of_manufacture=2015, fuel_type="Diesel", insurance_provider="Allstate",
        insurance_policy_number="POL123", last_service_date=datetime(2023, 6, 15), notes="No issues",
        bus_id="B001"
    )
    df = pd.read_csv(TEST_BUSES_CSV)
    assert len(df) == 1
    assert df.loc[0, "bus_type"] == "Standard"

@patch("backend.services.utils.STUDENTS_CSV", TEST_STUDENTS_CSV)
def test_create_initial_csv(setup_test_files):
    headers = ["id", "name", "age"]
    create_initial_csv(TEST_STUDENTS_CSV, headers)
    df = pd.read_csv(TEST_STUDENTS_CSV)
    assert list(df.columns) == headers