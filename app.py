"""
from flask import Flask, request, jsonify
import os
from pipelines.data_preprocessing import process_audio
from pipelines.model_training import authenticate_voice, analyze_sentiment
from database import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/voice_biometric'
db.init_app(app)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.form
    name = data.get('name')
    email = data.get('email')
    audio_file = request.files['audio']
    
    if not name or not email or not audio_file:
        return jsonify({"error": "Missing required fields"}), 400
    
    file_path = os.path.join("uploads", f"{email}.wav")
    audio_file.save(file_path)
    processed_audio = process_audio(file_path)
    
    new_user = User(name=name, email=email, voice_data=processed_audio)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "Signup successful!"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    email = data.get('email')
    audio_file = request.files['audio']
    
    if not email or not audio_file:
        return jsonify({"error": "Missing required fields"}), 400
    
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found, please signup"}), 404
    
    file_path = os.path.join("uploads", f"temp_{email}.wav")
    audio_file.save(file_path)
    
    if authenticate_voice(user.voice_data, file_path):
        return jsonify({"message": "Authentication successful!"}), 200
    else:
        return jsonify({"error": "Voice authentication failed"}), 401

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.form
    email = data.get('email')
    audio_file = request.files['audio']
    
    if not email or not audio_file:
        return jsonify({"error": "Missing required fields"}), 400
    
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found, please signup"}), 404
    
    file_path = os.path.join("uploads", f"temp_auth_{email}.wav")
    audio_file.save(file_path)
    
    if authenticate_voice(user.voice_data, file_path):
        return jsonify({"message": "Authentication successful!"}), 200
    else:
        return jsonify({"error": "Voice authentication failed"}), 401

@app.route('/sentiment', methods=['POST'])
def sentiment():
    audio_file = request.files['audio']
    if not audio_file:
        return jsonify({"error": "No audio file provided"}), 400
    
    file_path = os.path.join("uploads", "temp_sentiment.wav")
    audio_file.save(file_path)
    
    sentiment_result = analyze_sentiment(file_path)
    return jsonify({"sentiment": sentiment_result, "message": "Sentiment analysis completed."}), 200

if __name__ == '__main__':
    app.run(debug=True)

"""