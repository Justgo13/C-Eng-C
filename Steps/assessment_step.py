from Steps.base_step import BaseStep
import pytesseract
from datetime import date
import cv2

class AssessmentStep(BaseStep):

    def __init__(self):
        super().__init__("Self Test", "Scan your self test result", 100)
        TESS_DIR = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        pytesseract.pytesseract.tesseract_cmd = TESS_DIR
        pass

    def _run_step(self, image) -> int:
        today = date.today()
        today = '{0} {1}'.format(today.strftime('%B'), today.day).upper()
        text = pytesseract.image_to_string(image)
        h, w, _ = image.shape
        boxes = pytesseract.image_to_boxes(image)
        for b in boxes.splitlines():
            b = b.split(' ')
            cv2.rectangle(image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
            pass

        verified = today in text.upper()
        if verified:
            text = 'Thank you. The door will now open for you.'
            cv2.putText(image, text, (20, 30), cv2.FONT_HERSHEY_DUPLEX,
                        0.8, (30, 200, 30), 2, cv2.LINE_AA)
        else:
            text = 'Please show your COVID-19 self assessment'
            cv2.putText(image, text, (20, 30), cv2.FONT_HERSHEY_DUPLEX,
                    0.8, (30, 30, 200), 2, cv2.LINE_AA)

        return BaseStep.SUCCESS if verified else BaseStep.RUNNING

    pass

