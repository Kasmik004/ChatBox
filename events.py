from extensions import socketio
from flask import Blueprint, request, render_template, redirect, url_for
from models.Users import User, ChatBox, Chats
from extensions import db

@socketio.on("connect")
def handle_connect():
    print("Client Connected")
#edit
@socketio.on("new_message")
def handle_new_message(message, current_box, current_user):
        user = User.query.filter_by(name=current_user).first()
        box = ChatBox.query.filter_by(chat_box_name=current_box).first()
        print("done boss")
        chat = Chats(chat=message,u_id=user.id,chat_box_id=box.chat_box_id)
        db.session.add(chat)
        db.session.commit()
        print("done boss") 
        url = "/home/box/{user}/{box}".format(user=current_user, box=current_box)
        #return render_template(url_for('home.box',current_box=current_box,current_user=current_user))

        socketio.emit('add_new_message', data={"chat": chat.chat, "user": current_user})
    

