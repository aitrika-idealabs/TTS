import streamlit as st
import requests

# Streamlit UI setup
st.title("Text-to-Speech Conversion")
st.write("Enter text, and convert it into speech using the Text-to-Speech API.")

# Input fields for the API endpoint and API key
api_url = st.secrets["api_url"]  # Text-to-Speech API URL
api_key = st.secrets["api_key"]  # API Key

# Text input field
input_text = st.text_area("Enter the text to convert to speech", height=200)

# Voice option (if supported by the API, you can customize this further)
voice = st.selectbox("Select a voice (if applicable)", ["default"])  # Customize if more voices are available
format_option = st.radio("Select audio format", ["mp3", "wav", "ogg"])  # Customize based on API capability

# Button to trigger the conversion
if st.button("Convert to Speech") and input_text:
    with st.spinner("Generating speech..."):
        # API headers
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # Request payload
        payload = {
            "text": input_text,
            "voice": voice,  # Modify this based on the API's expected structure
            "format": format_option
        }

        # Send POST request to the API
        response = requests.post(api_url, headers=headers, json=payload)

        if response.status_code == 200:
            # Save and play the audio file
            audio_content = response.content
            audio_file = f"generated_audio.{format_option}"
            
            with open(audio_file, "wb") as f:
                f.write(audio_content)

            st.success("Speech generated successfully!")
            st.audio(audio_file, format=f"audio/{format_option}")
        else:
            st.error(f"Failed to generate speech. Status Code: {response.status_code}")
            st.write(response.text)
