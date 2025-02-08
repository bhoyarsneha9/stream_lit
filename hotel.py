import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Travel Planner", page_icon="✈️", layout="wide")

# Title
st.title("🌍 Travel Planner - Your Ultimate Travel Companion")

# Sidebar for Navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Choose a Service:", 
                           ["Home", "Hotels", "Homestays", "Tour Guides", "Travel Vehicles", "Itinerary Planner"])

# Dummy Data for Demonstration
hotels = pd.DataFrame({
    "Hotel Name": ["Radisson blue", "OYO PCrown", "Chandni"],
    "Location": ["Nagpur", "Amaravati", "Wanadongri"],
    "Price per Night": ["Rs 10000", "Rs 499", "Rs 900"],
    "Rating": ["⭐️⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️⭐️", "⭐️⭐️⭐️"]
})

homestays = pd.DataFrame({
    "Homestay Name": ["Homestay A", "Homestay B", "Homestay C"],
    "Location": ["Nagpur", "Amaravati", "Wanadongri"],
    "Price per Night": ["Rs 10000", "Rs 499", "Rs 900"],
    "Rating": ["⭐️⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️⭐️", "⭐️⭐️⭐️"]
})

tour_guides = pd.DataFrame({
    "Guide Name": ["John Doe", "Jane Smith", "Alice Johnson"],
    "Location": ["City X", "City Y", "City Z"],
    "Experience": ["5 years", "8 years", "3 years"],
    "Rating": ["⭐️⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️⭐️", "⭐️⭐️⭐️"]
})

vehicles = pd.DataFrame({
    "Vehicle Type": ["Car", "Bike", "Scooter"],
    "Price per Day": ["$50", "$30", "$20"],
    "Availability": ["Yes", "No", "Yes"]
})

# Home Page
if options == "Home":
    st.header("Welcome to Travel Planner!")
    st.write("Plan your trip with ease using our services:")
    st.write("- 🏨 Find Hotels")
    st.write("- 🏡 Book Homestays")
    st.write("- 🧭 Hire Tour Guides")
    st.write("- 🚗 Rent Travel Vehicles")
    st.write("- 📅 Auto Itinerary Planner")

# Hotel Finding System
elif options == "Hotels":
    st.header("🏨 Find Hotels")
    st.write("Explore the best hotels in your destination:")
    st.dataframe(hotels)

    # Filter by Location
    location = st.selectbox("Select Location:", ["City X", "City Y", "City Z"])
    filtered_hotels = hotels[hotels["Location"] == location]
    st.write(f"Hotels in {location}:")
    st.dataframe(filtered_hotels)

# Homestays
elif options == "Homestays":
    st.header("🏡 Book Homestays")
    st.write("Find cozy homestays for your stay:")
    st.dataframe(homestays)

    # Filter by Location
    location = st.selectbox("Select Location:", ["City X", "City Y", "City Z"])
    filtered_homestays = homestays[homestays["Location"] == location]
    st.write(f"Homestays in {location}:")
    st.dataframe(filtered_homestays)

# Tour Guide Information
elif options == "Tour Guides":
    st.header("🧭 Hire Tour Guides")
    st.write("Find experienced tour guides for your trip:")
    st.dataframe(tour_guides)

    # Filter by Location
    location = st.selectbox("Select Location:", ["City X", "City Y", "City Z"])
    filtered_guides = tour_guides[tour_guides["Location"] == location]
    st.write(f"Tour Guides in {location}:")
    st.dataframe(filtered_guides)

# Travel Vehicle Booking
elif options == "Travel Vehicles":
    st.header("🚗 Rent Travel Vehicles")
    st.write("Book vehicles for your travel:")
    st.dataframe(vehicles)

    # Filter by Availability
    availability = st.selectbox("Select Availability:", ["Yes", "No"])
    filtered_vehicles = vehicles[vehicles["Availability"] == availability]
    st.write(f"Available Vehicles: {availability}")
    st.dataframe(filtered_vehicles)

# Auto Itinerary Planner
elif options == "Itinerary Planner":
    st.header("📅 Auto Itinerary Planner")
    st.write("Plan your trip itinerary automatically:")

    # Input Fields
    destination = st.text_input("Enter Destination:")
    start_date = st.date_input("Start Date:")
    end_date = st.date_input("End Date:")
    interests = st.multiselect("Select Interests:", ["Adventure", "Sightseeing", "Food", "Shopping", "Relaxation"])

    if st.button("Generate Itinerary"):
        if destination and start_date and end_date and interests:
            st.success("Here's your itinerary:")
            st.write(f"**Destination:** {destination}")
            st.write(f"**Trip Duration:** {start_date} to {end_date}")
            st.write(f"**Interests:** {', '.join(interests)}")
            st.write("**Day 1:** Arrival and Check-in")
            st.write("**Day 2:** Sightseeing and Local Food Tour")
            st.write("**Day 3:** Adventure Activities")
            st.write("**Day 4:** Shopping and Relaxation")
            st.write("**Day 5:** Departure")
        else:
            st.error("Please fill in all the fields!")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Made with ❤️ by TRIPIT")
