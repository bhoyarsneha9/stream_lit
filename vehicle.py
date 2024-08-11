import streamlit as st
from datetime import datetime, timedelta

# Function to calculate the next maintenance date
def calculate_next_maintenance(last_date, interval_days):
    return last_date + timedelta(days=interval_days)

# Vehicle Maintenance Reminders App
st.title("Vehicle Maintenance Reminders and DIY Guides")

st.sidebar.header("Set Up Maintenance Reminders")

# Input fields for setting reminders
maintenance_task = st.sidebar.selectbox("Select Maintenance Task", ["Oil Change", "Tire Rotation", "Brake Inspection"])
last_maintenance_date = st.sidebar.date_input("Last Maintenance Date", datetime.now())
maintenance_interval_days = st.sidebar.number_input("Maintenance Interval (days)", min_value=1, max_value=365, value=90)

# Calculate the next maintenance date
next_maintenance_date = calculate_next_maintenance(last_maintenance_date, maintenance_interval_days)

# Display the next maintenance date
st.sidebar.write(f"Next {maintenance_task}: {next_maintenance_date.strftime('%Y-%m-%d')}")

# Display a list of common DIY guides
st.header("DIY Guides for Vehicle Maintenance")

diy_guides = {
    "Oil Change": "1. Gather tools and supplies.\n2. Drain the old oil.\n3. Replace the oil filter.\n4. Add new oil.\n5. Check for leaks.",
    "Tire Rotation": "1. Loosen the lug nuts.\n2. Lift the car with a jack.\n3. Rotate the tires.\n4. Lower the car and tighten the lug nuts.",
    "Brake Inspection": "1. Remove the wheel.\n2. Inspect brake pads and rotors.\n3. Check for any signs of wear or damage.\n4. Reassemble the wheel.",
}

# Display the selected DIY guide
selected_guide = st.selectbox("Select a Maintenance Task for DIY Guide", list(diy_guides.keys()))
st.subheader(f"DIY Guide for {selected_guide}")
st.text(diy_guides[selected_guide])

# Add some more information about safety
st.info("Always ensure you have the correct tools and follow safety precautions while performing vehicle maintenance.")

# Display a reminder to schedule professional inspections
st.warning("For complex maintenance tasks or if you're unsure about the procedure, consult a professional mechanic.")
