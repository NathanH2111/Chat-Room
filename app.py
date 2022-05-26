from flask import *
from flask_socketio import *

app = Flask(__name__)
appClient = SocketIO(app)

@app.route('/')
def renderLogin():
    return render_template('login.html')

@app.route('/login', methods=["GET", "POST"])
def defineUser():
    if request.method == 'POST':
        userName = request.form.get('UserName')
        roomID = request.form.get('RoomID')
        return redirect(url_for('renderChatroom', userName=userName, roomID=roomID))

@app.route('/chatroom')
def renderChatroom():
    userName = request.args.get('userName')
    roomID = request.args.get('roomID')
    return render_template('chatroom.html', userName=userName, roomID=roomID)

if __name__ == '__main__': appClient.run(app)