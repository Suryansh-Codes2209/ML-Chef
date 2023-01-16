from flask import Flask, render_template, redirect, url_for, request, Response
from camera import Video
from camera1 import Video1
from camera2 import Video2

application = Flask(__name__)


@application.route("/")
def index():
    return render_template('index.html')


@application.route("/mlintro")
def mlintro():
    return render_template('ml-intro.html')


@application.route("/faceintro")
def faceintro():
    return render_template('facedetectintro.html')


@application.route("/hand")
def hand():
    return render_template('handdetect.html')


def gen2(camera2):
    while True:
        frame2 = camera2.get_frame2()
        yield (b'--frame2\r\n'
               b'Content-Type:  image/jpeg\r\n\r\n' + frame2 +
               b'\r\n\r\n')


@application.route("/eye")
def eye():
    return render_template('eyedetect.html')


def gen1(camera1):
    while True:
        frame1 = camera1.get_frame1()
        yield (b'--frame1\r\n'
               b'Content-Type:  image/jpeg\r\n\r\n' + frame1 +
               b'\r\n\r\n')


@application.route("/facedetect")
def facedetect():
    return render_template('facedetect.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type:  image/jpeg\r\n\r\n' + frame +
               b'\r\n\r\n')


@application.route('/video')
def video():
    return Response(gen(Video()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@application.route('/video1')
def video1():
    return Response(gen1(Video1()),
                    mimetype='multipart/x-  mixed-replace; boundary=frame')


@application.route('/video2')
def video2():
    return Response(gen2(Video2()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    application.run(debug=True)
