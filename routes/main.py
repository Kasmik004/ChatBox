from flask import Blueprint, render_template, session, request, redirect, url_for, flash, sessions
from extensions import db
from models.Users import User, Chats, ChatBox
from flask_session import Session
from models.video import Video
main = Blueprint('main', __name__)




@main.route('/')
@main.route('/login')
def login():
    if not session.get("username"):
        return render_template("login.html", err=0)
    else:
        boxs = ChatBox.query.all()
        user = User.query.filter_by(name=session["username"]).first()
        return render_template("home.html", data=user, boxes=boxs)


@main.route('/login/auth', methods = ['POST','GET'])
def l_auth():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(name=username).first()
    if user:
        if (user.password == password):
            boxs = ChatBox.query.all()
            session["username"] = user.name
            return render_template("home.html", data = user, boxes = boxs)
        else:

            return render_template("login.html", err=1)

    else:

        return render_template("login.html", err=-1)


@main.route('/register')
def reg():
    return render_template('register.html')


@main.route('/register/auth', methods = ['POST','GET'])
def reg_auth():
        username = request.form['username']
        password = request.form['password']

        user = User(name=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect('/main/')

@main.route('/logout')
def logout():
    session['username'] = None
    session['user_data']=None
    return render_template("login.html", err=0)

