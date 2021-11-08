# ProjectGurukul Face mask Detector
# Source: https://projectgurukul.org/face-mask-detection/

# Import necessary packages
import os

import cv2
import uuid
import mediapipe as mp
from misc.misc import get_git_root

# Define mediapipe Face detector
face_detection = mp.solutions.face_detection.FaceDetection(0.6)

# Detection function
def get_detection(frame):
    
    height, width, channel = frame.shape

    # Convert frame BGR to RGB colorspace
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Detect results from the frame
    result = face_detection.process(imgRGB)
    
    # Extract data from result
    try:
        for count, detection in enumerate(result.detections):
            # print(detection)
        
            # Extract bounding box information 
 
            box = detection.location_data.relative_bounding_box
            x, y, w, h = int(box.xmin*width), int(box.ymin * height), int(box.width*width), int(box.height*height)
            
    # If detection is not available then pass 
    except:
        pass

    return x, y, w, h


cap = cv2.VideoCapture(0)
count = 0

class_path = 'mask' # values are mask and no_mask
git_root = get_git_root()
while True:
    _, frame = cap.read()
    img = frame.copy()
    try:
        # Make detection
        x, y, w, h = get_detection(frame)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
        # Crop only the face part from the frame
        crop_img = img[y:y+h, x:x+w]
        filename = os.path.join(git_root, "face-mask-detection", "Data", class_path, str(uuid.uuid4())) + ".jpg"

        print(filename)
        # Save the image to the destination path
        x1 = cv2.imwrite(filename, crop_img)
        print(x1)
        x = cv2.imshow("frame", crop_img)
        count+=1
    except:
        pass
    if cv2.waitKey(1) == ord('q') or count>=500:
        break
    
cap.release()
cv2.destroyAllWindows()




