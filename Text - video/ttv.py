import streamlit as st
import requests

API_KEY = "c3dhdGhpc2VtbWFuYW45MUBnbWFpbC5jb20:ZdnyACOT0eFRUOD4cb3YW"  
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

st.title("Text to Video (Avatar)")

text_input = st.text_input("Enter text for the avatar to speak:")

if st.button("Generate Video") and text_input.strip() != "":
    payload = {
        "script": {
            "type": "text",
            "input": text_input,
            "provider": {"type": "microsoft", "voice_id": "en-US-JennyNeural"}  # Optional but recommended
        },
        "source_url": "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"
    }

    response = requests.post("https://api.d-id.com/talks", json=payload, headers=HEADERS)

    if response.status_code == 200:
        video_url = response.json().get("result_url")
        st.video(video_url)
    else:
        st.error(f"Video generation failed: {response.status_code} - {response.text}")
