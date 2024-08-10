import streamlit as st
import datetime

# In-memory storage for medications
if 'medications' not in st.session_state:
    st.session_state.medications = []

# Helper function to add medication
def add_medication(name, time):
    st.session_state.medications.append({'name': name, 'time': time})

# Helper function to delete medication
def delete_medication(index):
    if 0 <= index < len(st.session_state.medications):
        st.session_state.medications.pop(index)

st.title("Medication Reminder and Tracker")

# Form for adding new medication
with st.form(key='med_form'):
    name = st.text_input('Medication Name', max_chars=100)
    time = st.time_input('Reminder Time', datetime.time(8, 0))  # Default to 8:00 AM
    submit_button = st.form_submit_button(label='Add Medication')

    if submit_button:
        if name:
            add_medication(name, time.strftime('%H:%M'))
            st.success(f'Medication "{name}" added for {time.strftime("%H:%M")}.')
        else:
            st.error('Please enter a medication name.')

# Display medications
st.subheader('Medication List')

if st.session_state.medications:
    for i, med in enumerate(st.session_state.medications):
        col1, col2, col3 = st.columns([3, 2, 1])
        with col1:
            st.write(f'{med["name"]}')
        with col2:
            st.write(f'{med["time"]}')
        with col3:
            if st.button('Delete', key=i):
                delete_medication(i)
                st.experimental_rerun()  # Refresh the app to update the list
else:
    st.write('No medications added yet.')
