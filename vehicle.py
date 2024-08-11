import streamlit as st
import pandas as pd
import datetime

# Fake data for vehicle maintenance reminders
maintenance_data = {
    'Task': ['Oil Change', 'Tire Rotation', 'Brake Inspection', 'Air Filter Replacement', 'Battery Check'],
    'Last Completed': [datetime.date(2024, 1, 15), datetime.date(2024, 2, 10), datetime.date(2024, 3, 5), datetime.date(2024, 4, 20), datetime.date(2024, 5, 18)],
    'Frequency (Days)': [90, 180, 365, 180, 365]
}

# Fake data for tire comparison
tire_data = {
    'Tire Model': ['All-Season A1', 'Winter Grip X2', 'Performance P3', 'Off-Road R4', 'Eco-Friendly E5'],
    'Car Model': ['Sedan', 'SUV', 'Sports Car', 'Truck', 'Hybrid'],
    'Driving Habits': ['Daily Commute', 'Snowy Roads', 'High Speed', 'Off-Road', 'Fuel Efficiency'],
    'Climate Conditions': ['Mild', 'Snowy', 'Mild', 'Harsh', 'Mild'],
    'User Reviews': [4.5, 4.7, 4.2, 4.8, 4.9],
    'Expert Recommendations': ['Recommended', 'Highly Recommended', 'Recommended', 'Highly Recommended', 'Recommended']
}

def calculate_next_due_date(last_completed, frequency):
    return last_completed + datetime.timedelta(days=frequency)

# Navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Maintenance Scheduling & DIY Repair Guides", "Tire Selection & Comparison Tool"])

if selection == "Maintenance Scheduling & DIY Repair Guides":
    st.title("Maintenance Scheduling & DIY Repair Guides")
    
    # Maintenance Reminders Section
    st.header("Vehicle Maintenance Reminders")
    st.write("Set up and manage reminders for essential vehicle maintenance tasks.")

    maintenance_df = pd.DataFrame(maintenance_data)
    maintenance_df['Next Due Date'] = maintenance_df.apply(lambda row: calculate_next_due_date(row['Last Completed'], row['Frequency (Days)']), axis=1)
    st.dataframe(maintenance_df)

    # DIY Guides
    st.subheader("DIY Maintenance Guides")
    st.write("""
    - **Oil Change**: [How to change your oil](https://www.example.com/oil-change-guide)
    - **Tire Rotation**: [How to rotate your tires](https://www.example.com/tire-rotation-guide)
    - **Brake Inspection**: [How to inspect your brakes](https://www.example.com/brake-inspection-guide)
    - **Air Filter Replacement**: [How to replace your air filter](https://www.example.com/air-filter-guide)
    - **Battery Check**: [How to check your battery](https://www.example.com/battery-check-guide)
    """)

elif selection == "Tire Selection & Comparison Tool":
    st.title("Tire Selection & Comparison Tool")
    
    # Tire Comparison Tool
    st.write("Find the best tire options based on your vehicle model, driving habits, and local climate conditions.")

    tire_df = pd.DataFrame(tire_data)
    st.dataframe(tire_df)

    # Tire selection filter
    car_model = st.selectbox("Select Car Model", tire_df['Car Model'].unique())
    filtered_tires = tire_df[tire_df['Car Model'] == car_model]
    st.dataframe(filtered_tires)

# Footer
st.sidebar.write("For more information, visit our [website](https://www.example.com).")






