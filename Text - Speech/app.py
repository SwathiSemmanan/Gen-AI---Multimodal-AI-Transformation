
from gtts import gTTS
import streamlit as st
import os

st.title("Text-to-Speech App")
text_input = st.text_input("Enter text:")

if st.button("Convert to Speech"):
    if text_input:
        tts = gTTS(text_input)
        tts.save("output.mp3")
        st.audio("output.mp3", format="audio/mp3")