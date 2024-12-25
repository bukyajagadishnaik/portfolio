# app/__init__.py
from flask import Flask
from .routes import create_routes

from flask_mail import Mail
app = Flask(__name__)
app.config.from_object('config')  # Loads settings from config.py

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dummytestnoreply01@gmail.com'
app.config['MAIL_PASSWORD'] = 'nkvv pgvw vzrt desq'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True   

# Initialize routes
create_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
