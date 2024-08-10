import streamlit as st
import pandas as pd
from datetime import datetime, time

# Initialize session state
if 'medications' not in st.session_state:
    st.session_state.medications = []

def add_medication(name, dosage, frequency, time):
    st.session_state.medications.append({
        'name': name,
        'dosage': dosage,
        'frequency': frequency,
        'time': time
    })

st.title('Medication Reminder and Tracker')

# Add new medication
st.header('Add New Medication')
med_name = st.text_input('Medication Name')
med_dosage = st.text_input('Dosage')
med_frequency = st.selectbox('Frequency', ['Daily', 'Weekly', 'Monthly'])
med_time = st.time_input('Time', value=time(8, 0))

if st.button('Add Medication'):
    add_medication(med_name, med_dosage, med_frequency, med_time)
    st.success('Medication added successfully!')

# Display medication list
st.header('Your Medications')
if st.session_state.medications:
    df = pd.DataFrame(st.session_state.medications)
    st.table(df)
else:
    st.info('No medications added yet.')

# Check for due medications
st.header('Medication Reminders')
current_time = datetime.now().time()
for med in st.session_state.medications:
    if med['time'] <= current_time:
        st.warning(f"Time to take {med['name']} - {med['dosage']}")

# Basic statistics
st.header('Medication Statistics')
st.write(f"Total medications: {len(st.session_state.medications)}")
frequencies = pd.DataFrame(st.session_state.medications)['frequency'].value_counts()
st.write("Frequency distribution:")
st.write(frequencies)
