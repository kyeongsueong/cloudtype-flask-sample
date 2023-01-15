from flask import Flask, request, redirect, render_template, url_for, Response
import cv2
app = Flask(__name__)

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
        
@app.route("/")
def index():
    getDatas = "hihi"
    photo = f"/img/1.jpeg"
    return render_template('./index.html', getDatas=getDatas, photo=photo)
@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
