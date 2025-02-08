import streamlit as st
import random
import pandas as pd
from datetime import datetime

# Load existing user data
try:
    user_data = pd.read_csv("users.csv")
except:
    user_data = pd.DataFrame(columns=["Name", "Age", "Gender", "Preference", "Dark_Answers", "Timestamp"])

st.title("🔥 Dark Humor Matchmaking 💘")

# User Input
name = st.text_input("Your Name")
age = st.number_input("Your Age", min_value=18, max_value=100, step=1)
gender = st.selectbox("Your Gender", ["Male", "Female", "Other"])
preference = st.selectbox("Your Preference", ["Straight", "Gay", "Lesbian", "Bisexual", "Pansexual", "Other"])

# Dark Humor Questions
st.subheader("Answer these dark humor questions 😈")
questions = [
    "If you had to commit a crime, what would it be?",
    "What’s the worst thing you've ever laughed at?",
    "If you were a serial killer, what would be your nickname?"
]
answers = []
for q in questions:
    answers.append(st.text_input(q, ""))

dark_answers = ", ".join(answers)

# Submit Button
if st.button("Submit and Find Matches 💘"):
    if name and age and gender and preference:
        # Save User
        new_data = pd.DataFrame([[name, age, gender, preference, dark_answers, datetime.now()]],
                                columns=user_data.columns)
        user_data = pd.concat([user_data, new_data], ignore_index=True)
        user_data.to_csv("users.csv", index=False)
        st.success("Profile Submitted! Now Finding Your Match...")
    else:
        st.error("Please fill in all details!")

# Show Existing Users
st.subheader("💖 Meet Other Singles")
st.dataframe(user_data)

# Matchmaking System
st.subheader("💥 Compatibility Calculator")
p1 = st.selectbox("Select Person 1", user_data["Name"].tolist())
p2 = st.selectbox("Select Person 2", user_data["Name"].tolist())

if st.button("Calculate Compatibility 🔥"):
    if p1 != p2:
        match_percentage = random.randint(10, 100)
        st.write(f"💞 {p1} & {p2} are {match_percentage}% compatible!")
        
        if match_percentage > 80:
            st.balloons()
            st.write("💥 BOOM! It's a match made in heaven! 💘")
    else:
        st.error("Select two different people!")
