import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import os

# Set Streamlit page config
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Function to load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to apply local CSS
def local_css(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply custom CSS for background
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background: url("https://source.unsplash.com/random/1920x1080/?technology") no-repeat center fixed;
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# Load CSS file (ensure "style/style.css" exists)
local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_xontact_form = Image.open("images/Bankruptcy.jpg")
img_lottie_animation = Image.open("images/Opiod stock photo.jpg")
img_animation_from = Image.open("images/Netflix.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Agath Clafio :wave:")
    st.title("A Data Scientist")
    st.write(
        "Motivated and results-driven Computer Science graduate. Proficient in Machine Learning models, data analysis, and SQL. Passionate about extracting insights and predicting trends."
    )
    st.write("[Learn More >](https://www.linkedin.com/in/agathclafio/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            As a data scientist with six months of experience: 
            - Cleaning and preprocessing data
            - Conducting Exploratory Data Analysis (EDA)
            - Building and evaluating machine learning models
            - Communicating insights through data visualization
            """
        )
        st.write("[GitHub >](https://github.com/AgathClafio05)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    
    # Project 1
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Drug Satisfaction Predictor")
        st.write(
            """
            Developed a predictor achieving 85% accuracy in forecasting drug satisfaction rates. 
            Built and deployed as a web app to aid in medical treatment decision-making.
            """
        )
        st.markdown("[Explore Project](https://github.com/AgathClafio05/project-01)")
    
    # Project 2
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_xontact_form)
        with text_column:
            st.subheader("Bankruptcy Prediction")
            st.write(
                """
                Built an ML model (96.9% accuracy) predicting business bankruptcy.
                Integrated into a web interface for easy business risk assessment.
                """
            )
            st.markdown("[Explore Project](https://github.com/AgathClafio05/project-02)")
    
    # Project 3
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_animation_from)
        with text_column:
            st.subheader("Netflix Recommendation")
            st.write(
                """
                Conducted data analysis on Netflix dataset. Implemented clustering and 
                built a recommendation system using cosine similarity.
                """
            )
            st.markdown("[Explore Project](https://github.com/AgathClafio05/project-03)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
   <form action="https://formsubmit.co/agathclafio55@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
   </form>
    """
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
