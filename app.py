import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import os

# Set Streamlit page config
st.set_page_config(page_title="My Portfolio", page_icon="🌟", layout="wide")

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

# Apply custom CSS for modern background
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
            color: white;
            font-family: 'Arial', sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# Load CSS file
local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_project_1 = Image.open("images/Bankruptcy.jpg")
img_project_2 = Image.open("images/Opiod_stock.jpg")
img_project_3 = Image.open("images/Netflix.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.markdown("<div class='glassmorphism'><h1>👋 Hi, I'm Agath Clafio</h1></div>", unsafe_allow_html=True)
    st.subheader("A Passionate Data Scientist")
    st.write(
        "I analyze data, build ML models, and create AI-powered solutions. Let's turn data into insights!"
    )
    st.markdown("<a class='button' href='https://www.linkedin.com/in/agathclafio/' target='_blank'>🔗 LinkedIn</a>", unsafe_allow_html=True)

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("<div class='glassmorphism'><h2>🚀 What I Do</h2></div>", unsafe_allow_html=True)
        st.write(
            """
            - 📊 Data Cleaning & Preprocessing  
            - 📈 Exploratory Data Analysis  
            - 🤖 Machine Learning Model Building  
            - 📡 Deploying AI Models as Web Apps  
            """
        )
        st.markdown("<a class='button' href='https://github.com/AgathClafio05' target='_blank'>📂 GitHub</a>", unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
st.write("---")
st.markdown("<div class='glassmorphism'><h2>🌟 My Projects</h2></div>", unsafe_allow_html=True)

# Project 1
image_column, text_column = st.columns((1, 2))
with image_column:
    st.image(img_project_1, width=250)
with text_column:
    st.markdown("<h3>💰 Bankruptcy Prediction</h3>", unsafe_allow_html=True)
    st.write("An AI model with 96.9% accuracy predicting business bankruptcy.")
    st.markdown("<a class='button' href='https://github.com/AgathClafio05/project-01' target='_blank'>🔍 View Project</a>", unsafe_allow_html=True)

# Project 2
image_column, text_column = st.columns((1, 2))
with image_column:
    st.image(img_project_2, width=250)
with text_column:
    st.markdown("<h3>💊 Drug Satisfaction Predictor</h3>", unsafe_allow_html=True)
    st.write("Built an AI predictor with 85% accuracy for drug satisfaction rates.")
    st.markdown("<a class='button' href='https://github.com/AgathClafio05/project-02' target='_blank'>🔍 View Project</a>", unsafe_allow_html=True)

# Project 3
image_column, text_column = st.columns((1, 2))
with image_column:
    st.image(img_project_3, width=250)
with text_column:
    st.markdown("<h3>🎬 Netflix Recommendation</h3>", unsafe_allow_html=True)
    st.write("A recommendation system using clustering & cosine similarity.")
    st.markdown("<a class='button' href='https://github.com/AgathClafio05/project-03' target='_blank'>🔍 View Project</a>", unsafe_allow_html=True)

# ---- CONTACT ----
st.write("---")
st.markdown("<div class='glassmorphism'><h2>📬 Get In Touch</h2></div>", unsafe_allow_html=True)

contact_form = """
<form action="https://formsubmit.co/agathclafio55@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your Message Here" required></textarea>
    <button type="submit">Send Message</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
