import streamlit as st
import cohere

# Initialize Cohere client with your API key directly
cohere_api_key = "SjyS7xPZqAisqztLmaHBf3VwjsxWShRrgcEBKxeu"
co = cohere.Client(cohere_api_key)

# Function to get response from Cohere
def get_cohere_response(question):
    response = co.chat(
        model='command', 
        message=question,
        max_tokens=100,
        temperature=0.5
    )
    return response.text

# Streamlit app setup
st.set_page_config(page_title="Q&A Demo")
st.header("Cohere Q&A Bot")

input_question = st.text_input("Input your question:")
submit = st.button("Ask")

if submit and input_question:
    st.subheader("The Response is:")
    st.write(get_cohere_response(input_question))