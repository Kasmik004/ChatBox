from flask import Flask
from extensions import db

from routes.main import main
from routes.api import home

from events import socketio
#new comment
app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'hard to guess string'
print("configured with database")
db.init_app(app)
app.register_blueprint(main, url_prefix="/main")
app.register_blueprint(home, url_prefix="/home")
socketio.init_app(app)


def create_tables():
    with app.app_context():
        db.create_all()






if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
    socketio.run(app)