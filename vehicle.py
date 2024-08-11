import streamlit as st
from datetime import datetime, timedelta

# Function to calculate the next maintenance date
def calculate_next_maintenance(last_date, interval_days):
    return last_date + timedelta(days=interval_days)

# Fake data for tires
fake_tire_data = [
    {"Brand": "Brand A", "Model": "All-Season X", "Tread Life": "60,000 miles", "Performance": "Good", "Price": "$120", "Rating": 4.5},
    {"Brand": "Brand B", "Model": "Winter Y", "Tread Life": "50,000 miles", "Performance": "Excellent", "Price": "$140", "Rating": 4.7},
    {"Brand": "Brand C", "Model": "Summer Z", "Tread Life": "45,000 miles", "Performance": "High", "Price": "$150", "Rating": 4.9},
    {"Brand": "Brand D", "Model": "Performance Q", "Tread Life": "40,000 miles", "Performance": "Outstanding", "Price": "$180", "Rating": 4.8},
    {"Brand": "Brand E", "Model": "Off-Road P", "Tread Life": "70,000 miles", "Performance": "Very Good", "Price": "$160", "Rating": 4.6}
]

# Fake data for car troubleshooting
fake_troubleshooting_data = {
    "Strange Noise": {
        "Issue": "Possible loose belt or worn bearings",
        "Solution": "Check belts for wear and tighten them. Inspect bearings and replace if necessary."
    },
    "Engine Overheating": {
        "Issue": "Coolant leak or malfunctioning radiator",
        "Solution": "Check coolant levels and inspect the radiator for leaks. Replace any faulty parts."
    },
    "Brake Warning Light": {
        "Issue": "Worn brake pads or low brake fluid",
        "Solution": "Check brake pads and replace if worn. Ensure brake fluid is at the correct level."
    },
    "Car Won't Start": {
        "Issue": "Dead battery or faulty starter",
        "Solution": "Test the battery and replace if necessary. Check the starter for any issues."
    },
    "Vibration While Driving": {
        "Issue": "Unbalanced tires or alignment issues",
        "Solution": "Have the tires balanced and check the vehicle's alignment."
    }
}

# Navigation options
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Maintenance Scheduling & Repair Guides", "Tire Selection & Comparison", "Interactive Car Troubleshooting Guide"])

# Section 1: Maintenance Scheduling & Repair Guides
if page == "Maintenance Scheduling & Repair Guides":
    st.title("Maintenance Scheduling & Repair Guides")

    # Sidebar for Maintenance Reminders
    st.sidebar.header("Set Up Maintenance Reminders")
    task = st.sidebar.text_input("Enter Maintenance Task", "Oil Change")
    last_date = st.sidebar.date_input("Last Maintenance Date", datetime.now())
    interval = st.sidebar.number_input("Maintenance Interval (days)", min_value=1, max_value=365, value=90)

    next_date = calculate_next_maintenance(last_date, interval)
    st.sidebar.write(f"Next {task}: {next_date.strftime('%Y-%m-%d')}")

    # Option to add additional maintenance schedules
    if st.sidebar.button("Add Another Task"):
        st.sidebar.text_input("Enter Another Maintenance Task", "Tire Rotation")
        st.sidebar.date_input("Last Maintenance Date", datetime.now())
        st.sidebar.number_input("Maintenance Interval (days)", min_value=1, max_value=365, value=180)

    # DIY Guides
    st.header("DIY Guides")
    guides = {
        "Oil Change": {
            "Steps": "1. Gather tools and supplies.\n2. Drain the old oil.\n3. Replace the oil filter.\n4. Add new oil.\n5. Check for leaks.",
            "Video": "https://youtu.be/O1hF25Cowv8?si=sohHVnnsafhoBr4k",
            "Tools": "Wrench, Oil filter, Funnel, Oil pan",
            "Safety Tips": "Always wear gloves and ensure the car is on a flat surface."
        },
        "Tire Rotation": {
            "Steps": "1. Loosen the lug nuts.\n2. Lift the car with a jack.\n3. Rotate the tires.\n4. Lower the car and tighten the lug nuts.",
            "Video": "https://youtu.be/_As8hQVqlvc?si=w6oqMURIfTE4H9fB",
            "Tools": "Jack, Lug wrench",
            "Safety Tips": "Use a jack stand for added safety."
        },
        "Brake Inspection": {
            "Steps": "1. Remove the wheel.\n2. Inspect brake pads and rotors.\n3. Check for any signs of wear or damage.\n4. Reassemble the wheel.",
            "Video": "https://youtu.be/_j6ZvsEBO7Y?si=XtC-RraxxOdXFFPf",
            "Tools": "Wrench, Jack, Brake cleaner",
            "Safety Tips": "Ensure the car is securely lifted and use proper tools."
        }
    }
    selected_guide = st.selectbox("Select a Maintenance Task for DIY Guide", list(guides.keys()))
    guide = guides[selected_guide]

    st.subheader(f"DIY Guide for {selected_guide}")
    st.text(guide["Steps"])
    st.markdown(f"[Watch Video]({guide['Video']})")
    st.text(f"Tools Needed: {guide['Tools']}")
    st.text(f"Safety Tips: {guide['Safety Tips']}")

# Section 2: Tire Selection & Comparison
elif page == "Tire Selection & Comparison":
    st.title("Tire Selection & Comparison")

    # Filters
    car_model = st.text_input("Enter Your Car Model")
    driving_habit = st.selectbox("Select Your Driving Habit", ["Daily Commute", "Off-Road", "Performance"])
    climate_condition = st.selectbox("Select Climate Condition", ["All-Season", "Winter", "Summer"])

    # Filter and display tire options based on user selection
    filtered_tires = [
        tire for tire in fake_tire_data
        if tire["Performance"] == driving_habit or tire["Model"].split()[0] == climate_condition
    ]

    st.subheader("Available Tire Options")
    if filtered_tires:
        for tire in filtered_tires:
            st.write(f"**Brand:** {tire['Brand']}")
            st.write(f"**Model:** {tire['Model']}")
            st.write(f"**Tread Life:** {tire['Tread Life']}")
            st.write(f"**Performance:** {tire['Performance']}")
            st.write(f"**Price:** {tire['Price']}")
            st.write(f"**Rating:** {tire['Rating']} stars")
            st.write("---")
    else:
        st.write("No tires found matching your criteria.")

# Section 3: Interactive Car Troubleshooting Guide
elif page == "Interactive Car Troubleshooting Guide":
    st.title("Interactive Car Troubleshooting Guide")

    # Symptoms selection
    symptom = st.selectbox("Select the Symptom Your Car is Experiencing", list(fake_troubleshooting_data.keys()))
    issue_info = fake_troubleshooting_data[symptom]

    # Display the potential issue and solution
    st.subheader(f"Potential Issue: {issue_info['Issue']}")
    st.write(f"**Suggested Solution:** {issue_info['Solution']}")

    st.info("Always ensure safety while diagnosing or repairing your vehicle. If in doubt, seek professional help.")







