import os
import streamlit as st
from google import genai

# Page Title Setup
# https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config
# st.set_page_config(page_title="Bervin", page_icon=":up:", layout="centered", initial_sidebar_state="auto", menu_items=None) 

st.title("Why are you not doing work?\nBy Bervin")
client = genai.Client(api_key="AIzaSyAKqHDLoSN1Rs9yvrCOlJO2bPQXBhLNook")

### Generate a pre-defined prompt ###
response = client.models.generate_content(
    model='gemini-2.0-flash', 
    contents='Tell me 1 fun fact about gemini ai in 8 words.'
)
st.write(response.text)


### Generate a pre-defined prompt ###
qns = st.text_input(label="Ask Gemini Questions")

if st.button("Submit"):
    response2 = client.models.generate_content(
    model='gemini-2.0-flash', 
    contents=qns
    )
    st.write(response2.text)

