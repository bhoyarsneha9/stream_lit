import streamlit as st
import random
import pandas as pd
from datetime import datetime

# Load existing user data
students = [
    "BALI MANJIRI RAJESH", "GAIKWAD PRACHITI YOGESH", "RUCHITA NAGESHRAO GURUDWAR", "JAD SAKSHI AJAY", 
    "RAULKAR SAMPADA MADAN", "KHAN SANA NASIR", "SHIWANGI RATHORE", "WANDHARE SHRAVIKA MANOJ", 
    "LADKE SHREYA SHRIKRUSHNA", "THAKARE SHREYA DILIPRAO", "NANDANWAR SHREYA MANOJ", "DHOLE SMRUTI DEVENDRA", 
    "BHOYAR SNEHA SHAILESH", "SUHANI MANOJ URKUDE", "SADAWARTI SUKANYA MEGHRAJ", "PUSATE SUMEDHA RAVINDRA", 
    "KHANDRE SWARANGI SANJAY", "SHENDE TANISHKA VILAS", "MAHAJAN TANUSHRI PURUSHOTTAM", "AMBAGADE UNNATI ASHOK", 
    "PATIL UTKARSHA VIVEK", "PATTANAYAK ARNAB ARBINDA", "BHADADE ASHISH ANIL", "BAMNOTE DHIRAJ MOTILAL", 
    "SHEIKH FARDIN ZAHIR", "GAURAV PRANAY KOKASH", "BELE JAYESH DAMODHAR", "MOHAMMAD TAEB SHAKEEL AHMED", 
    "SAWAI MOHIT KISHOR", "YELNE PRAJYOT PRASHANT", "UDAPURKAR RACHIT RAJENDRA", "GODSUNDARE SAHIL MUKUND", 
    "MITKARI SAI MANGESH", "KHANDARE SANCHIT HEMANT", "NAHATE SANDESH NITESH", "SINGH SAURABH ATUL", 
    "SUKALKAR SHAILESH RAJESH", "SARVE SHASHANK DAYAL", "SHUBH JHA", "PHALKE SOHAM MANGESH", 
    "REWATKAR SPANDAN ANAND", "PANSE SUBODH DHANANJAY", "GUPTA SUJAL RAJESH", "DHAGE SUJAL SANJAY", 
    "RANGARI SUJAL ANIL", "MESHRAM SURENDRA VIJAY", "GAWANDE SWARUP AJAY", "TAMBOLI SWAYAM SUBHASHRAO", 
    "SHRIKHANDE TEJAS PRASHANT", "BARMASE TEJAS RAJENDRA", "TEMBHURKAR UDAY BHARAT", "NARNAWARE VANSH ISHWAR", 
    "VITANKAR VEDANT SANJAY", "BOGAWAR VEDANT MILIND", "PARATE VEDDHANT CHANDRAKANT", "KHAWANE YADNYESH RAJENDRA", 
    "UTANE YASH SATISH", "BORSARE YASH MILIND", "CHANNE YASH NARESH", "KHADSE YASH RAMRAO", "BAMBAL YUGANT SEVAKRAM"
]

df = pd.DataFrame(students, columns=["Name"])
df["Timestamp"] = datetime.now()

st.title("🔥 TRYME 🫦")

# Compatibility Calculator
st.subheader("💥 Compatibility Calculator")
p1 = st.selectbox("Select Person 1", df["Name"].tolist())
p2 = st.selectbox("Select Person 2", df["Name"].tolist())

if st.button("Calculate Compatibility 🔥"):
    if p1 != p2:
        match_percentage = random.randint(10, 100)
        st.write(f"💞 {p1} & {p2} are {match_percentage}% compatible!")
        
        if match_percentage > 80:
            st.balloons()
            st.write("💥 BOOM! It's a match made in heaven! 💘")
    else:
        st.error("Select two different students!")

# Questionnaire Section
st.subheader("📝 Answer Some Fun Questions")
age = st.number_input("Enter Your Age", min_value=18, max_value=100, step=1)
gender = st.selectbox("Your Gender", ["Male", "Female", "Other"])
preference = st.selectbox("Your Preference", ["Straight", "Gay", "Lesbian", "Bisexual", "Pansexual", "Other"])

questions = [
    "What's your darkest humor joke?",
    "If you had to commit a crime, what would it be?",
    "What’s the worst thing you've ever laughed at?",
    "If you were a serial killer, what would be your nickname?"
]
answers = []
for q in questions:
    answers.append(st.text_input(q, ""))

dark_answers = ", ".join(answers)

if st.button("Submit My Answers"):
    st.success("Your answers have been recorded!")

# Hidden User Data Section
with st.expander("🔍 View All Registered Users"):
    st.dataframe(df)
