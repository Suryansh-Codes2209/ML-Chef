import cv2

cascade_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')

class Video1(object):
    def __init__(self):
        self.video1=cv2.VideoCapture(0)
    def __del__(self):
        self.video1.release()
    def get_frame1(self):
        ret, frame1=self.video1.read()
        detections = cascade_classifier.detectMultiScale(frame1,scaleFactor=1.3,minNeighbors=5)
        for (x,y,w,h) in detections:
            frame1 = cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),2)


        ret,jpg=cv2.imencode('.jpg',frame1)
        return jpg.tobytes()
            


























    



