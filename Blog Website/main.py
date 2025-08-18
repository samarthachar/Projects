from flask import Flask, render_template, request
import requests
import sendMail

name = None
email = None
phone_number = None
message = None

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html" , h1text=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/contact', methods=["POST"])
def receive_data():

    global name, email, phone_number, message

    name = request.form["name"]
    email = request.form["email"]
    phone_number = request.form["phone"]
    message = request.form["message"]
    bot = sendMail.MailBot(name, email, phone_number, message)
    return render_template("contact.html", h1text=True)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
