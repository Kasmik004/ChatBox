from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    chats = db.relationship('Chats', backref='user')

class Chats(db.Model):
    chat_id = db.Column(db.Integer, primary_key=True)
    chat = db.Column(db.String(255))
    chat_box_id = db.Column(db.Integer, db.ForeignKey('chat_box.chat_box_id'))
    u_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #user = db.relationship('User', backref=db.backref('chats', lazy='dynamic'))
    chat_box = db.relationship('ChatBox', backref=db.backref('chats', lazy='dynamic'))

class ChatBox(db.Model):
    chat_box_id = db.Column(db.Integer, primary_key=True)
    chat_box_name = db.Column(db.String(50))
