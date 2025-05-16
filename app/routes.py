# app/routes.py
from flask import render_template ,request, send_from_directory 
from flask_mail import Mail , Message

# Avoid circular import by importing `app` inside a route function
def create_routes(app):
    @app.route('/home')
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/download_cv')
    def download_cv():
        return send_from_directory(directory='static', path='B_JagadishNaik_resume.pdf', as_attachment=True)
    
    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/projects')
    def projects():
        return render_template('projects.html')

    @app.route('/contact', methods=["GET","POST"])
    def contact():
        if request.method == "GET":
            return render_template("contact.html")
        elif request.method == "POST":
            mail = Mail(app)
            name = request.form["name"]
            email = request.form['email']
            phone = request.form['phone']
            message = request.form['message']
            if email :
                customer = [email]     
                msgbody = f"""
Dear {name},

Thank you for taking the time to visit my portfolio website and share your valuable feedback. I truly appreciate your thoughtful insights.

Your insights have provided me with meaningful ideas for improvement, and I’m always eager to refine and enhance my work. Please don’t hesitate to reach out if you have any additional suggestions or questions—I’d be happy to continue the conversation.

Thank you once again for your support and encouragement.

Warm regards,
Bukya Jagadish Naik"""
            msg = Message("Thank You for Your Feedback", sender='noreplay@demo.com' ,recipients=customer)
            msg.body = msgbody
            mail.send(msg)
            print("name :" ,name)
            print("Message :",message)
        return render_template('contact.html')
    
    @app.route('/services')
    def services():
        return render_template('services.html')
