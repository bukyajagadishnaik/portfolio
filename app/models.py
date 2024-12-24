# app/models.py
import sqlite3

DATABASE = 'portfolio.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    return db

def get_projects():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM projects')
    return cursor.fetchall()
