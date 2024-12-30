from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'lohitha'  # Secure the session

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'lohithakshi113@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'acxwurpeneyjbjfu'     # Replace with your app-specific password

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send_email", methods=["POST"])
def send_email():
    # Get data from form
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # If any field is missing, show an error message
    if not name or not email or not message:
        flash("All fields are required!", "error")
        return redirect("/")

    # Create and send email message
    msg = Message(
        subject=f"New Contact Message from {name}",
        sender=email,
        recipients=["lohithakshi113@gmail.com"],  # Replace with your email
        body=f"Name: {name}\nEmail: {email}\nMessage: {message}"
    )

    try:
        mail.send(msg)
        flash("Message sent successfully!", "success")
    except Exception as e:
        flash(f"Error sending message: {e}", "error")

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
