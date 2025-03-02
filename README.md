# Voice Recognition Biometric System

## Introduction
The **Voice Recognition Biometric System** is an AI-powered application that provides **secure authentication**, **real-time sentiment analysis**, and **personalized motivational quotes** based on voice input. This system leverages **Flask**, **Streamlit**, **MySQL**, **Natural Language Processing (NLP)**, **TensorFlow/Keras**, and **scikit-learn** for advanced voice recognition and emotion detection.

## Features
- **Voice Authentication:** Secure access through voice biometrics.
- **Sentiment Analysis:** Real-time emotion detection from voice input.
- **Personalized Quotes:** AI-driven motivational quotes tailored to detected emotions.

## Tech Stack
- **Backend:** Flask, Streamlit
- **Frontend:** Streamlit UI
- **Database:** MySQL
- **Machine Learning:** TensorFlow/Keras, scikit-learn
- **NLP & Speech Processing:** OpenAI Whisper, Google Speech API, CMU Sphinx

## System Architecture
1. **Voice Input:** User speaks into a microphone.
2. **Voice Authentication:** System verifies identity using biometric voice patterns.
3. **Sentiment Analysis:** AI model classifies emotion from speech.
4. **Quote Recommendation:** System selects and displays a relevant quote.

## Authentication & Workflow
### **Signup Process:**
1. **Record Voice (Password Sentence):** User speaks a predefined sentence for authentication.
2. **Record Again:** The system verifies consistency in the voice sample.
3. **Input Name & Email ID:** User provides identity details, which are stored securely.

### **Login Process:**
1. **Input Name & Email ID:** User enters credentials and records voice for authentication.
2. **Database Matching:** System checks if user exists in the database.
3. **Record Found & Voice Matched?** → ✅ **Authenticate & Grant Access**
4. **Record Found & Voice Not Matched?** → ❌ **Authentication Failed**
5. **Record Not Found?** → Suggests **Signup Process**
6. **If Authentication is Successful:**
   - Perform **Sentiment Analysis** on the recorded voice.
   - Generate & display a **motivational quote** based on detected emotion.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- MySQL
- Virtual Environment (optional but recommended)

### Setup Instructions
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/04bhavyaa-voice-recognition-biometric-system.git
   cd 04bhavyaa-voice-recognition-biometric-system
   ```
2. **Create a Virtual Environment (Optional):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Setup MySQL Database:**
   - Create a MySQL database:
     ```sql
     CREATE DATABASE voice_biometric;
     ```
   - Update the `.env` file with your database credentials:
     ```ini
     DB_HOST=localhost
     DB_USER=root
     DB_PASSWORD=yourpassword
     DB_NAME=voice_biometric
     ```
5. **Run Migrations (If Using Flask-Migrate):**
   ```bash
   flask db upgrade
   ```
6. **Start the Flask Backend:**
   ```bash
   python app.py
   ```
7. **Run Streamlit for UI (In a Separate Terminal):**
   ```bash
   streamlit run ui.py
   ```

## Usage
- **User Authentication:** Speak into the microphone to log in.
- **Emotion Detection:** The system will analyze your voice tone and classify emotions.
- **Personalized Quotes:** Based on detected sentiment, a motivational quote will be displayed.

## Folder Structure
```
04bhavyaa-voice-recognition-biometric-system/
├── README.md                # Project documentation
├── LICENSE                  # License file
├── app.py                   # Main Flask backend
├── requirements.txt         # Project dependencies
├── ui.py                    # Streamlit UI
├── pipelines/               # Pipeline components
│   ├── data_preprocessing.py  # Data cleaning and preparation
│   ├── data_transformation.py # Feature engineering and transformation
│   └── model_training.py      # Model training and evaluation

# will be updated
```

## Future Improvements
- Improve accuracy of voice authentication using deep learning models.
- Optimize NLP models for better sentiment analysis.
- Extend to support multiple languages for emotion detection.

## Contributors

- **Bhavya Jha** ([bhavyajha1404@gmail.com](mailto\:bhavyajha1404@gmail.com))
- **Neha Sachdeva**
- **Akshita Arora**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
Feel free to contribute and improve the system! 🚀

