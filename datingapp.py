import streamlit as st
import pandas as pd

# Initialize session state
if 'users' not in st.session_state:
    st.session_state.users = []

# Helper function to add user
def add_user(name, neighborhood, bio):
    st.session_state.users.append({'name': name, 'neighborhood': neighborhood, 'bio': bio})

# Helper function to get matches
def find_matches(neighborhood):
    return [user for user in st.session_state.users if user['neighborhood'] == neighborhood]

# Streamlit app
st.title("Neighborhood Dating App")

# Form for adding a new user
with st.form(key='user_form'):
    name = st.text_input('Name')
    neighborhood = st.text_input('Neighborhood')
    bio = st.text_area('Bio')
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if name and neighborhood:
            add_user(name, neighborhood, bio)
            st.success(f'Profile created for {name} in {neighborhood}.')
        else:
            st.error('Please enter both name and neighborhood.')

# Display the list of users
st.subheader('Find Matches in Your Neighborhood')

neighborhood_input = st.text_input('Enter your neighborhood to find matches:')
if neighborhood_input:
    matches = find_matches(neighborhood_input)
    if matches:
        st.write(f'Users in {neighborhood_input}:')
        for user in matches:
            st.write(f"**Name:** {user['name']}")
            st.write(f"**Bio:** {user['bio']}")
            st.write('---')
    else:
        st.write(f'No users found in {neighborhood_input}.')

# Display all users
st.subheader('All Users')
if st.session_state.users:
    df = pd.DataFrame(st.session_state.users)
    st.dataframe(df)
else:
    st.write('No users added yet.')
