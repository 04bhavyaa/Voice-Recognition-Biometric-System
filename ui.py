"""
import streamlit as st
import requests
import sounddevice as sd
import numpy as np
import wave

API_URL = "http://127.0.0.1:5000"

st.title("🎤 Voice Recognition Biometric System")

# Record and save audio function
def record_audio(filename="audio.wav", duration=5, fs=44100):
    st.info("Recording...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(audio_data.tobytes())
    st.success("Recording complete!")

# Authentication
st.subheader("🔐 Voice Authentication")
if st.button("Record & Authenticate"):
    record_audio("auth_audio.wav")
    with open("auth_audio.wav", "rb") as f:
        response = requests.post(f"{API_URL}/authenticate", files={"audio": f})
    result = response.json()
    st.write("Authenticated" if result["authenticated"] else "Authentication Failed!")
    if result["authenticated"]:
        st.success(f"Welcome, {result['user']}!")

# Sentiment Analysis
st.subheader("😊 Sentiment Analysis")
if st.button("Record & Analyze Emotion"):
    record_audio("emotion_audio.wav")
    with open("emotion_audio.wav", "rb") as f:
        response = requests.post(f"{API_URL}/analyze_sentiment", files={"audio": f})
    result = response.json()
    st.write(f"Detected Emotion: {result['sentiment']}")
    st.success(f"Quote: {result['quote']}")
"""