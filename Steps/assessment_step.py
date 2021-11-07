from Steps.base_step import BaseStep
import pytesseract
from datetime import date
import cv2

class AssessmentStep(BaseStep):

    def __init__(self):
        super().__init__("Self Test", "Scan your self test result", 15)
        TESS_DIR = '/usr/bin/tesseract'
        pytesseract.pytesseract.tesseract_cmd = TESS_DIR
        pass

    def _run_step(self, image) -> int:
        today = date.today()
        today = '{0} {1}'.format(today.strftime('%B'), today.day).upper()
        text = pytesseract.image_to_string(image)
        image = cv2.flip(image, 1)
        h, w, _ = image.shape
        boxes = pytesseract.image_to_boxes(image)
        for b in boxes.splitlines():
            b = b.split(' ')
            image = cv2.rectangle(image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
            pass
        return AssessmentStep.SUCCESS if today in text.upper() else AssessmentStep.RUNNING

    pass

