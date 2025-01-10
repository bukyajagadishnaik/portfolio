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
        return send_from_directory(directory='static', path='Bukya_jagadish_Naik_Resume.pdf', as_attachment=True)
    
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
Hi {name},
Thank you so much for visiting my portfolio website and taking the time to send me your feedback and suggestions! I truly appreciate your thoughts on [specific suggestion or message they sent].

Your insights have given me some great ideas to consider, and I'm always looking to improve my work. If you have any further suggestions or questions, feel free to reach out—I’d love to continue the conversation.
            
Thanks again for your support!

Best regards,
Bukya Jagadish Naik """
            msg = Message("Thank You for Your Feedback on My Portfolio", sender='noreplay@demo.com' ,recipients=customer)
            msg.body = msgbody
            mail.send(msg)
            print("name :" ,name)
            print("Message :",message)
        return render_template('contact.html')
    
    @app.route('/services')
    def services():
        return render_template('services.html')
