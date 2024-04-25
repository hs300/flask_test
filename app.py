from flask import Flask, url_for, request, render_template
from markupsafe import escape
from flask.blueprints import Blueprint

from auth import auth_bp
app = Flask(__name__)

print(__name__)


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


@app.get('/loginget')
def test_get():
    print(request.method)
    return "xxx"


@app.post('/loginpost')
def test_post():
    print(request.method)
    return "aaaaaaaa"


@app.route('/testrender')
def testrender():
    return render_template('test.html')


user = Blueprint('user', __name__)


@user.route('/user')
def testprint():
    return 'testprint'


app.register_blueprint(user)

app.register_blueprint(auth_bp)
