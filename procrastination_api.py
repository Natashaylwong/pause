import cv2
import math
import numpy as np
import dlib
from sklearn.externals import joblib

emotions = ["anger", "disgust", "happiness", "neutral", "surprise"]
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clf = joblib.load('model.skl')

landmark_num = 68
predictor_file = "shape_predictor_68_face_landmarks.dat"

video_capture = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_file)


def convert_to_cv2(filename):
    return cv2.imread(filename)


def image_prediction(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_image = clahe.apply(gray)
    detections = detector(clahe_image, 1)

    for k, d in enumerate(detections):
        shape = predictor(clahe_image, d)

        xlist = []
        ylist = []
        for i in range(1, landmark_num):
            xlist.append(float(shape.part(i).x))
            ylist.append(float(shape.part(i).y))

            cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (0, 0, 255), thickness=2)

        xmean = np.mean(xlist)
        ymean = np.mean(ylist)
        xcentral = [(x - xmean) for x in xlist]
        ycentral = [(y - ymean) for y in ylist]

        landmarks_vectorised = np.array([])
        for x, y, w, z in zip(xcentral, ycentral, xlist, ylist):
            landmarks_vectorised.append(w)
            landmarks_vectorised.append(z)
            meannp = np.asarray((ymean, xmean))
            coornp = np.asarray((z, w))
            dist = np.linalg.norm(coornp - meannp)
            landmarks_vectorised.append(dist)
            landmarks_vectorised.append((math.atan2(y, x) * 360) / (2 * math.pi))
        landmarks_vectorised = np.array(landmarks_vectorised)

    prediction = clf.predict(landmarks_vectorised.reshape(1, -1))[0]
    cv2.imshow("image", frame)

    return emotions[prediction]


def video_predict(iterations):
    prediction = -1
    landmarks_vectorised = np.array([0 for _ in range(268)])

    while iterations > 0:
        frame = video_capture.read()[1]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        clahe_image = clahe.apply(gray)
        detections = detector(clahe_image, 1)

        for k, d in enumerate(detections):
            shape = predictor(clahe_image, d)

            xlist = []
            ylist = []
            for i in range(1, landmark_num):
                xlist.append(float(shape.part(i).x))
                ylist.append(float(shape.part(i).y))

                cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (0, 0, 255), thickness=2)

            xmean = np.mean(xlist)
            ymean = np.mean(ylist)
            xcentral = [(x - xmean) for x in xlist]
            ycentral = [(y - ymean) for y in ylist]

            landmarks_vectorised = []
            for x, y, w, z in zip(xcentral, ycentral, xlist, ylist):
                landmarks_vectorised.append(w)
                landmarks_vectorised.append(z)
                meannp = np.asarray((ymean, xmean))
                coornp = np.asarray((z, w))
                dist = np.linalg.norm(coornp - meannp)
                landmarks_vectorised.append(dist)
                landmarks_vectorised.append((math.atan2(y, x) * 360) / (2 * math.pi))
            landmarks_vectorised = np.array(landmarks_vectorised)

        previous = prediction
        prediction = clf.predict(landmarks_vectorised.reshape(1, -1))[0]
        cv2.imshow("image", frame)

        if prediction != previous:
            print(emotions[prediction])

        iterations -= 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    video_predict(float('inf'))
