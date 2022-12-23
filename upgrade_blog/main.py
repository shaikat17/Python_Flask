from flask import Flask, render_template, request
import smtplib
import requests

app = Flask(__name__)

posts = requests.get('https://api.npoint.io/217117266f430a3e22db').json()

@app.route("/")
def home():
    return render_template('index.html', all_post = posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_email(name, email, phone, message)
        print('Mail Sent')

        return "<h1>Your data sent successfully</h1>"
    return render_template('contact.html')


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, Receiver_EMAIL, email_message)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
