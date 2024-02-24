from extensions import socketio

@socketio.on("connect")
def handle_connect():
    print("Client Connected")


@socketio.on("new_message")
def handle_new_message(message, current_box, current_user):
    pass

