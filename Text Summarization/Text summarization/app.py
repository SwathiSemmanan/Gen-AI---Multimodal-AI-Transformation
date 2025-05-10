import streamlit as st
import cohere

# Replace with your real Cohere API key
API_KEY = "SjyS7xPZqAisqztLmaHBf3VwjsxWShRrgcEBKxeu"

# Initialize Cohere client
co = cohere.Client(API_KEY)

st.title("📝 Text Summarization with Cohere")
st.markdown("Summarize large texts quickly using Cohere's AI model.")

# Text input
input_text = st.text_area("Enter the text you want to summarize:", height=250)

# Select summary length
summary_length = st.selectbox("Choose summary length:", ["short", "medium", "long"])

# Select format
summary_format = st.selectbox("Choose format:", ["paragraph", "bullets"])

if st.button("Summarize"):
    if input_text.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            try:
                response = co.summarize(
                    text=input_text,
                    length=summary_length,
                    format=summary_format,
                    model="summarize-xlarge"
                )
                st.success("Summary:")
                st.write(response.summary)
            except Exception as e:
                st.error(f"Error: {str(e)}")