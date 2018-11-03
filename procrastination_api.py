import cv2
import glob
import random
import math
import numpy as np
import dlib
from sklearn.svm import SVC

emotions = ["anger", "contempt", "disgust", "fear", "happiness", "neutral", "sadness", "surprise"]
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clf = SVC(kernel='linear', probability=True, tol=1e-3)

landmark_num = 68
predictor_file = "shape_predictor_68_face_landmarks.dat"

video_capture = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_file)


def get_landmarks(image):
    detections = detector(image, 1)
    for k, d in enumerate(detections):
        shape = predictor(image, d)
        xlist = []
        ylist = []
        for i in range(1, 68):
            xlist.append(float(shape.part(i).x))
            ylist.append(float(shape.part(i).y))

        xmean = np.mean(xlist)
        ymean = np.mean(ylist)
        xcentral = [(x-xmean) for x in xlist]
        ycentral = [(y-ymean) for y in ylist]

        landmarks_vectorised = []
        for x, y, w, z in zip(xcentral, ycentral, xlist, ylist):
            landmarks_vectorised.append(w)
            landmarks_vectorised.append(z)
            meannp = np.asarray((ymean, xmean))
            coornp = np.asarray((z, w))
            dist = np.linalg.norm(coornp-meannp)
            landmarks_vectorised.append(dist)
            landmarks_vectorised.append((math.atan2(y, x)*360)/(2*math.pi))

    return landmarks_vectorised


def video_collect(clf, iterations):
    detected = False
    previous = False

    while iterations > 0:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        clahe_image = clahe.apply(gray)
        detections = detector(clahe_image, 1)

        for k, d in enumerate(detections):
            shape = predictor(clahe_image, d)
            for i in range(1, landmark_num):
                cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (0, 0, 255), thickness=2)
            detected = True

        if not detected and previous:
            print("Face Lost")
            previous = False

        cv2.imshow("image", frame)

        if detected and not previous:
            print("Face Detected")
            previous = True

        detected = False
        iterations -= 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def video_predict(clf, iterations):
    detected = False
    previous = False

    while iterations > 0:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        clahe_image = clahe.apply(gray)
        detections = detector(clahe_image, 1)

        for k, d in enumerate(detections):
            shape = predictor(clahe_image, d)
            for i in range(1, landmark_num):
                cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (0, 0, 255), thickness=2)
            detected = True

        if not detected and previous:
            print("Face Lost")
            previous = False

        cv2.imshow("image", frame)

        if detected and not previous:
            print("Face Detected")
            previous = True

        detected = False
        iterations -= 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
