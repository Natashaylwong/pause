from flask import Flask, request
import procrastination_api as procrastination
import base64
import os

app = Flask(__name__)
image_name = "face.png"


@app.route("/predict")
def predict():
    img_data = request.args.get('img')
    with open("face.png", "wb") as fh:
        fh.write(base64.decodebytes(img_data))

    frame = procrastination.convert_to_cv2("face.png")
    os.remove("face.png")

    prediction = procrastination.image_prediction(frame)

    return prediction


if __name__ == "__main__":
    app.run()
