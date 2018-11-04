from flask import Flask, request, jsonify
import flask
import procrastination_api as procrastination
import base64
import os

from PIL import Image

app = Flask(__name__)
image_name = "face.png"


@app.route("/predict")
def predict():
    img_data = str(request)[71:-8].replace("%2F", "/")

    img_file = open(image_name, "wb")
    img_file.write(base64.urlsafe_b64decode(img_data))
    img_file.close()

    frame = procrastination.convert_to_cv2(image_name)
    os.remove(image_name)

    prediction = procrastination.image_prediction(frame)
    print(prediction)

    resp = flask.Response(prediction)
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp


if __name__ == "__main__":
    app.run()
