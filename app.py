import streamlit as st
from pathlib import Path
import base64
import os
import pandas as pd

def home_page():
    current_dir = Path(__file__).parent
    background_image = current_dir / "background_image.jpeg"
    with open(background_image, "rb") as f:
        image_bytes = f.read()
    encoded_image = base64.b64encode(image_bytes).decode()
    
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
    }}
    .stFileUploader > div > div > div > div {{
        color: black; /* Set input text color to black */
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)
    # Title and Welcome Message
    st.title("Welcome to :red[Kick-Start-Up!]")
    st.markdown("<div style='background-color: white; padding: 10px;'>""<p style='color: darkblue; font-size: 20px;'>""Connecting Social Impact Projects with Potential Investors""</p>""</div>",
    unsafe_allow_html=True)

    # Description
    st.markdown(
    "<div style='background-color: lightblue; padding: 10px;'>"
    "<p style='color: black; font-size: 20px;'>"
    "Kick-Start-Up is a platform dedicated to fostering sustainability and driving positive change. "
    "We bridge the gap between social impact projects and investors who are passionate about making a difference. "
    "Whether you're an investor looking to support impactful initiatives or an ideator seeking funding to bring your vision to life, "
    "Kick-Start-Up is your platform for sustainable change."
    "</p>"
    "</div>",
    unsafe_allow_html=True
    )

    # Buttons for Login
    # Buttons for Login with increased size
    col1, col2 = st.columns([2,2])
    ideatorlogin=col1.button("Login as Ideator")
    if ideatorlogin: 
        st.session_state['page'] = 'ideatorlogin'
    investorlogin=col2.button("Login as Investor")
    if investorlogin:
        st.session_state['page'] = 'investorlogin'

    # Custom CSS to increase button size
    st.markdown(
        """
        <style>
        div[data-testid="stButton"] > button {
            width: 200px; /* Adjust button width as needed */
            height: 50px; /* Adjust button height as needed */
            font-size: 20px; /* Adjust font size as needed */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def authenticate_user(username, password):
    df = pd.read_csv('ideators.csv')
    #hashed_password = hash_password(password)
    if ((df['username'] == username) & (df['password'] == password)).any():
        return True
    else:
        return False
    
def ideatorlogin():
    st.title("LOGIN AS :red[IDEATOR]")
    username = st.text_input("USER NAME")
    password = st.text_input("PASSWORD",type="password")
    login= st.button("LOG IN")
    if login:
        if authenticate_user(username, password):
            st.session_state['page'] = 'ideate'
        else:
            st.error("Invalid username or password.")
    st.write("<div style='text-align: center;'><p style='font-size: 24px;'>New  user ? Dont have  an  account</p> </div>", unsafe_allow_html=True)
    col1,col2,col3=st.columns([2,2,1])
    ideatorsignup=col2.button("SIGN UP AS IDEATOR")
    if ideatorsignup:
        st.session_state['page'] = 'ideatorsignup'

def ideatorsignup():
    st.title("Sign Up as Ideator")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    if st.button("Create Account"):
         add_user(new_username, new_password)
         st.session_state['page'] = 'home'

# Function to add a new user to CSV
def add_user(username, password):
    df = pd.DataFrame({'username': [username], 'password': [password]})
    df.to_csv('ideators.csv', mode='a', index=False)

def ideate():
    st.title("Ideate")
    
def main():
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'

    if st.session_state['page'] == 'home':
        home_page()
    elif st.session_state['page'] == 'ideatorlogin':
        ideatorlogin()
    elif st.session_state['page'] == 'ideatorsignup':
        ideatorsignup()
    elif st.session_state['page'] == 'ideate':
        ideate()
    
    

if __name__== "__main__":
    main()