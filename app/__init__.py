# app/__init__.py
from flask import Flask
from .routes import create_routes

app = Flask(__name__)
app.config.from_object('config')  # Loads settings from config.py

# Initialize routes
create_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
