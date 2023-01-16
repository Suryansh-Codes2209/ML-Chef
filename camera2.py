import cv2
import mediapipe as mp


class Video2(object):
    def __init__(self):
        self.video2=cv2.VideoCapture(0)

    def __del__(self):
        self.video2.release()

    def get_frame2(self):
        ret, frame2=self.video2.read()
        # Draw the hand annotations on the image.
        mp_drawing = mp.solutions.drawing_utils
        mp_hands = mp.solutions.hands
        for hand_landmarks in cv2.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                cv2, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        ret, jpg=cv2.imencode('.jpg', frame2)
        return jpg.tobytes()
