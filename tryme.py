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

st.set_page_config(page_title="🔥 TRYME 🫦", page_icon="🔥", layout="wide")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Compatibility Test", "Random Matches", "Questionnaire", "Registered Users"])

if page == "Home":
    st.title("🔥 Welcome to TRYME 🫦")
    st.write("Find your perfect match based on your humor and personality!")

elif page == "Compatibility Test":
    st.subheader("💥 Compatibility Test Based on Questionnaire")
    st.write("Answer the questions below to find your best match!")
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
    
    if st.button("Submit My Answers"):
        match = random.choice(df["Name"].tolist())
        st.success(f"Based on your answers, your best match is: {match} 💖")

elif page == "Random Matches":
    st.subheader("💖 Get a Random Match")
    if st.button("Find My Random Match"):
        match = random.sample(df["Name"].tolist(), 2)
        st.write(f"✨ Your match is: {match[0]} & {match[1]} 💘")
        if random.randint(1, 100) > 80:
            st.balloons()

elif page == "Questionnaire":
    st.subheader("📝 Answer Some Fun Questions")
    for q in ["What's your darkest humor joke?", "If you had to commit a crime, what would it be?", "What’s the worst thing you've ever laughed at?", "If you were a serial killer, what would be your nickname?"]:
        st.text_input(q, "")
    
elif page == "Registered Users":
    st.subheader("🔍 View All Registered Users")
    st.dataframe(df)
