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

search_history = []

st.set_page_config(page_title="🔥 TRYME 🫦", page_icon="🔥", layout="wide")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Compatibility Test", "Random Matches", "Questionnaire", "Registered Users", "Name Compatibility", "Search History"])

if page == "Home":
    st.title("🔥 Welcome to TRYME 🫦")
    st.write("Find your perfect match based on your humor and personality!")

elif page == "Compatibility Test":
    st.subheader("💥 Compatibility Test Based on Questionnaire")
    st.write("Answer the questions below to find your best match!")
    age = st.number_input("Enter Your Age", min_value=18, max_value=100, step=1)
    gender = st.selectbox("Your Gender", ["Male", "Female", "Other"])
    preference = st.selectbox("Your Preference", ["Straight", "Gay", "Lesbian"])
    
    questions = [
        "What's your dark fantasy?", "How do you feel about sex outside?", "What’s the worst thing you've ever laughed at?", "What type of nude pictures would you like?","Are you a boob,ass or a dick person?"
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
            st.snow()

elif page == "Questionnaire":
    st.subheader("📝 Answer Some Fun Questions")
    for q in ["What's your dark fantasy?", "How do you feel about sex outside?", "What’s the worst thing you've ever laughed at?", "What type of nude pictures would you like?","Are you a boob,ass or a dick person?"]:
        st.text_input(q, "")
    
elif page == "Registered Users":
    st.subheader("🔍 View All Registered Users")
    st.dataframe(df)

elif page == "Name Compatibility":
    st.subheader("💕 Find Compatibility Between Two Names")
    name1 = st.selectbox("Select First Name", df["Name"].tolist())
    name2 = st.selectbox("Select Second Name", df["Name"].tolist())
    
    if st.button("Check Compatibility 💕"):
        if name1 != name2:
            compatibility = random.randint(10, 100)
            st.write(f"💞 {name1} & {name2} have a compatibility of {compatibility}%!")
            search_history.append((name1, name2, compatibility))
            if compatibility > 80:
                st.snow()
        else:
            st.error("Select two different names!")

elif page == "Search History":
    st.subheader("📜 Previous Searches")
    if search_history:
        for entry in search_history:
            st.write(f"{entry[0]} & {entry[1]} - {entry[2]}% Compatible")
    else:
        st.write("No searches yet!")
