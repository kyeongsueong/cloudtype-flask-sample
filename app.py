from flask import Flask, request, redirect, render_template, url_for, Response
from flask_socketio import SocketIO, send
import cv2


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)



def img_frames(frame):

    ret, buffer = cv2.imencode('.jpg', frame)
    print(buffer)
    frame = buffer.tobytes()
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

camera=cv2.VideoCapture(0)
def generate_frames():
    while True:

        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    getDatas = "hihi"
    photo = f"/img/1.jpeg"
    photo2 = f"/img/2.jpeg"
    return render_template("chat.html")

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast = True)

@app.route('/applyPoto')
def applyPoto():
    location = request.args.get("location")
    cleaenss = request.args.get("clean")
    print(location, cleaenss)
    return render_template("index.html")

@app.route('/upload_img', methods=["POST"])
def upload_img():
    upload_files = request.files["files"]
    upload_files.save("static/img/{}.jpeg".format(1))

    return render_template("index.html")

@app.route('/send_img', methods=["POST"])
def send_img():
    if request.method == "POST":
        lolo = request.files["img"]
        lolo.save("static/img/{}.jpeg".format(2))

        print(lolo)
        return Response(img_frames(lolo),mimetype='multipart/x-mixed-replace; boundary=frame')

#@app.route('/video')
#def video():
#    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
socketio.run(app)
#app.run(debug=True)
