import os
import smtplib, ssl
from flask_mail import Mail, Message
from flask import  Flask, render_template, request

# turn file to a web app.
app = Flask(__name__)

app.config['DEBUG'] = True

# list of trainees:
trainees = []
emails = []
goals = []

# listen on "/"
@app.route("/")

# "when accessing '/' return this"
def index():
    return render_template("index.html")


# mail_settings = {
#     "MAIL_SERVER": 'smtp.gmail.com',
#     "MAIL_PORT": 465,
#     "MAIL_USE_TLS": False,
#     "MAIL_USE_SSL": True,
#     "MAIL_USERNAME": os.environ['EMAIL_USER'],
#     "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
# }
#
# app.config.update(mail_settings)
# mail = Mail(app)


@app.route("/register", methods=["POST"])
def register():
    port = 587
    # dynamically getting users input for "name".
    name = request.form.get("name")
    goal = request.form.get("goal")
    email = request.form.get("email")
    trainees.append(name)
    emails.append(email)
    goals.append(goal)
    if not request.form.get("name") or not request.form.get("email") or not  request.form.get("goal"):
        return render_template("failure.html")
    message = "You are registered"
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    server = smtplib.SMTP("smtp.gmail.com",port)
    server.starttls(context=context)
    server.login("strongerbochka@gmail.com", "PASSWORD HERE")
    server.sendmail("strongerbochka@gmail.com", email, message)
    server.quit()
    return render_template("success.html")

@app.route("/registrants")
def registrants():
    return render_template("registered.html", trainees=trainees)



