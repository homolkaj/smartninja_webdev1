from flask import Flask, render_template, make_response, request, redirect
from sqla_wrapper import SQLAlchemy
import uuid
import hashlib

app = Flask(__name__)

db = SQLAlchemy("sqlite:///db.sqlite")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=False)
    sex = db.Column(db.String, unique=False)
    age = db.Column(db.Integer, unique=False)
    session_token = db.Column(db.String, unique=True)
    deleted = db.Column(db.Boolean, default=False)

db.create_all()

@app.route("/")
def index():
    session_token = request.cookies.get("session_token")

    if session_token:
        user = db.query(User).filter_by(session_token=session_token, deleted=False).first()
    else:
        user = None

    return render_template("index.html", user=user)

@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("user-name")
    email = request.form.get("user-email")
    sex = request.form.get("user-sex")
    age = request.form.get("user-age")
    password = request.form.get("user-password")

    # hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    user = db.query(User).filter_by(email=email).first()

    if not user:
        # create a User object
        user = User(name=name, email=email, sex=sex, age=age, password=hashed_password)
        user.save()

    # check if password is correct
    if hashed_password != user.password:
        return "WRONG PASSWORD! Go back and try again."
    elif hashed_password == user.password:
        # create a random session token for this user
        session_token = str(uuid.uuid4())
        print("created session token:", session_token)

        # save the session token in a database
        user.session_token = session_token
        user.save()

        # save user's session token into a cookie
        response = make_response(redirect('/'))
        response.set_cookie("session_token", session_token, httponly=True, samesite='Strict')

        return response

@app.route("/profile", methods=["GET"])
def profile():
    session_token = request.cookies.get("session_token")

    if session_token:
        user = db.query(User).filter_by(session_token=session_token, deleted=False).first()
    else:
        user = None

    if user:
        return render_template("profile.html", user=user)
    else:
        return redirect("/")


@app.route("/profile/edit", methods=["GET", "POST"])
def profile_edit():
    session_token = request.cookies.get("session_token")

    user = db.query(User).filter_by(session_token=session_token, deleted=False).first()

    if request.method == "GET":
        if user: # if user is found
            return render_template("profile_edit.html", user=user)
        else:
            return redirect("/")
    elif request.method == "POST":
        name = request.form.get("profile-name")
        email = request.form.get("profile-email")
        sex = request.form.get("profile-sex")
        age = request.form.get("profile-age")

        user.name = name
        user.email = email
        user.sex = sex
        user.age = age

        user.save()

        return redirect("/profile")


@app.route("/profile/delete", methods=["GET", "POST"])
def profile_delete():
    session_token = request.cookies.get("session_token")

    user = db.query(User).filter_by(session_token=session_token, deleted=False).first()

    if request.method == "GET":
        if user:
            return render_template("profile_delete.html", user=user)
        else:
            return redirect("/")
    elif request.method == "POST":
        # fake delete the user (mark the deleted field as True)
        user.deleted = True
        user.save()

        return redirect("/")


@app.route("/users", methods=["GET"])
def all_users():
    users = db.query(User).filter_by(deleted=False).all()  # find all un-deleted users

    return render_template("users.html", users=users)


@app.route("/user/<user_id>", methods=["GET"])
def user_details(user_id):
    user = db.query(User).get(int(user_id))  # .get() can help you query by the ID

    return render_template("user_details.html", user=user)

if __name__ == '__main__':
    app.run()