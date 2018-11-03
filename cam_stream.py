import cv2
import dlib

landmark_num = 68
predictor_file = "shape_predictor_68_face_landmarks.dat"

video_capture = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_file)


def main():
    endless_stream()
    video_capture.release()
    cv2.destroyAllWindows()


def video_stream(iterations):
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


def endless_stream():
    video_stream(float('inf'))

if __name__ == "__main__":
    main()
