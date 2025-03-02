"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    voice_data = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, name, email, voice_data):
        self.name = name
        self.email = email
        self.voice_data = voice_data

# Function to initialize the database
def init_db(app):
    with app.app_context():
        db.create_all()
        print("Database initialized successfully!")

"""