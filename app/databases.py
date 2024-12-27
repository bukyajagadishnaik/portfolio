import os ,sqlite3
from flask import g

DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'portfolio.db')


# Function to connect to the database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db