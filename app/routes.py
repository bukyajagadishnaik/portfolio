# app/routes.py
from flask import render_template

# Avoid circular import by importing `app` inside a route function
def create_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/projects')
    def projects():
        project_list = [
            {'title': 'Project 1', 'description': 'Description of Project 1', 'url': '#'},
            {'title': 'Project 2', 'description': 'Description of Project 2', 'url': '#'}
        ]
        return render_template('projects.html', projects=project_list)

    @app.route('/contact')
    def contact():
        return render_template('contact.html')
