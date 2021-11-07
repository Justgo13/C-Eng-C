import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

class FaceMaskDetector:
    def __init__(self):
        # Load the model
        self.model = load_model('face_mask_detection/model1.h5')
        # Load MediaPipe Face Detection
        self.face_detection = mp.solutions.face_detection.FaceDetection()

    def get_detection(self, frame):
        height, width, channel = frame.shape

        # Convert frame BGR to RGB colorspace

        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Detect results from the frame

        result = self.face_detection.process(imgRGB)

        try:
            for count, detection in enumerate(result.detections):
                # print(detection)

                # Extract bounding box information

                box = detection.location_data.relative_bounding_box

                x, y, w, h = int(box.xmin * width), int(box.ymin * height), int(box.width * width), int(box.height * height)

        # If detection is not available then pass
        except:
            pass

        return x, y, w, h

    def detect_face(self, frame):
        categories = ['mask', 'no_mask']
        res = 'neither'
        img = frame.copy()

        try:
            x, y, w, h = self.get_detection(frame)

            crop_img = img[y:y + h, x:x + w]

            crop_img = cv2.resize(crop_img, (100, 100))

            crop_img = np.expand_dims(crop_img, axis=0)

            # get the prediction from the model.
            prediction = self.model.predict(crop_img)

            index = np.argmax(prediction)
            res = categories[index]

            if index == 1:
                color = (0, 0, 255)
            else:
                color = (0, 255, 0)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, res, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, color, 2, cv2.LINE_AA)

        except:
            pass

        return (res, frame)


