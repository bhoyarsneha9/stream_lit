import streamlit as st
from datetime import datetime, timedelta

# Function to calculate the next maintenance date
def calculate_next_maintenance(last_date, interval_days):
    return last_date + timedelta(days=interval_days)

# Vehicle Maintenance Reminders and DIY Guides
st.title("Vehicle Maintenance and Tire Selection Tool")

# Sidebar for Maintenance Reminders
st.sidebar.header("Set Up Maintenance Reminders")

maintenance_task = st.sidebar.selectbox("Select Maintenance Task", ["Oil Change", "Tire Rotation", "Brake Inspection"])
last_maintenance_date = st.sidebar.date_input("Last Maintenance Date", datetime.now())
maintenance_interval_days = st.sidebar.number_input("Maintenance Interval (days)", min_value=1, max_value=365, value=90)

next_maintenance_date = calculate_next_maintenance(last_maintenance_date, maintenance_interval_days)
st.sidebar.write(f"Next {maintenance_task}: {next_maintenance_date.strftime('%Y-%m-%d')}")

# Display DIY Guides
st.header("DIY Guides for Vehicle Maintenance")

diy_guides = {
    "Oil Change": "1. Gather tools and supplies.\n2. Drain the old oil.\n3. Replace the oil filter.\n4. Add new oil.\n5. Check for leaks.",
    "Tire Rotation": "1. Loosen the lug nuts.\n2. Lift the car with a jack.\n3. Rotate the tires.\n4. Lower the car and tighten the lug nuts.",
    "Brake Inspection": "1. Remove the wheel.\n2. Inspect brake pads and rotors.\n3. Check for any signs of wear or damage.\n4. Reassemble the wheel.",
}

selected_guide = st.selectbox("Select a Maintenance Task for DIY Guide", list(diy_guides.keys()))
st.subheader(f"DIY Guide for {selected_guide}")
st.text(diy_guides[selected_guide])

st.info("Always ensure you have the correct tools and follow safety precautions while performing vehicle maintenance.")
st.warning("For complex maintenance tasks or if you're unsure about the procedure, consult a professional mechanic.")

# Tire Comparison and Selection Tool
st.header("Tire Comparison and Selection Tool")

# Example data for tires (In a real application, this data could be fetched from a database or API)
tires = [
    {"Brand": "Brand A", "Model": "Model X", "Climate": "All-Season", "Driving Habit": "Daily Commute", "Price": 100, "Rating": 4.5},
    {"Brand": "Brand B", "Model": "Model Y", "Climate": "Winter", "Driving Habit": "Off-Road", "Price": 120, "Rating": 4.7},
    {"Brand": "Brand C", "Model": "Model Z", "Climate": "Summer", "Driving Habit": "Performance", "Price": 150, "Rating": 4.9},
]

# Filters
car_model = st.text_input("Enter Your Car Model")
driving_habit = st.selectbox("Select Your Driving Habit", ["Daily Commute", "Off-Road", "Performance"])
climate_condition = st.selectbox("Select Climate Condition", ["All-Season", "Winter", "Summer"])

# Filter and display tires based on user selection
filtered_tires = [tire for tire in tires if tire["Driving Habit"] == driving_habit and tire["Climate"] == climate_condition]

st.subheader("Available Tire Options")
if filtered_tires:
    for tire in filtered_tires:
        st.write(f"**Brand:** {tire['Brand']}")
        st.write(f"**Model:** {tire['Model']}")
        st.write(f"**Price:** ${tire['Price']}")
        st.write(f"**Rating:** {tire['Rating']} stars")
        st.write("---")
else:
    st.write("No tires found matching your criteria.")

# User reviews and expert recommendations could be fetched from a database or API, but here we'll just simulate them
st.header("User Reviews and Expert Recommendations")
st.write("**User Review for Brand A Model X:** 'Great tire for daily commuting, provides smooth ride and good traction.'")
st.write("**Expert Recommendation:** 'For performance driving in summer conditions, Brand C Model Z offers the best handling and durability.'")

