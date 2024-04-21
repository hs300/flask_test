from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return "index page"


@app.route("/hello")
def hello3():
    return "hello"


@app.route("/user/<username>")
def show_user_profile(username):
    return username


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return {
        "post_id": post_id
    }


def wanger():
    return 'wang er'


with app.test_request_context():
    print("xxx")
    print(url_for('/hello'))

