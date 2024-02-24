from flask import Blueprint, request, render_template, redirect, url_for
from extensions import db
from models.Users import User
from models.video import Video
from models.Users import ChatBox, Chats
home = Blueprint('home', __name__)


@home.route('/<user>', methods=['POST','GET'])
def homepage(user):
    user = User.query.filter_by(name=user).first()
    boxes = ChatBox.query.all()

    return render_template('home.html', data=user, boxes=boxes)



@home.route('/box/<current_user>/<current_box>', methods=['POST','GET'])
def box(current_user,current_box):
    #chat_box = ChatBox.query.filter_by(chat_box_name=current_box).first()
    chats = db.session.query(Chats, User).\
            join(User).\
            join(ChatBox).\
            filter(ChatBox.chat_box_name == current_box).all()
    #chat_texts = [chat.chat for chat in chats]

    return render_template('chatbox.html', chats = chats,user_name = current_user, box_name=current_box)

@home.route('/chat_process/<current_user>/<current_box>', methods=['POST','GET'])
def chat_process(current_user,current_box):
        user = User.query.filter_by(name=current_user).first()
        box = ChatBox.query.filter_by(chat_box_name=current_box).first()
        chat = request.form['current_chat']

        chat = Chats(chat=chat,u_id=user.id,chat_box_id=box.chat_box_id)
        db.session.add(chat)
        db.session.commit()
        url = "/home/box/{user}/{box}".format(user=current_user, box=current_box)
        #return render_template(url_for('home.box',current_box=current_box,current_user=current_user))

        return redirect(url)





