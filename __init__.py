from flask import Flask
from extensions import db

from routes.main import main
from routes.api import home

from events import socketio

app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'hard to guess string'

db.init_app(app)
app.register_blueprint(main, url_prefix="/main")
app.register_blueprint(home, url_prefix="/home")
socketio.init_app(app)


def create_tables():
    with app.app_context():
        db.create_all()


#action="{{ url_for('home.chat_process', current_user=user_name,current_box=box_name) }}" method="POST"



if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
    socketio.run(app)