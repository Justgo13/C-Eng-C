import cv2

from Steps.base_step import BaseStep
from qr_code_detection.qr_code import draw_rectangle_on_QR, SUCCESS, FAIL


class VaccinePassportStep(BaseStep):

    def __init__(self):
        super().__init__("Vaccine Passport", "Scan the QR Code for your Proof of Vaccination", 15)
        self.counter = 0
        self.threshold = 10
        pass

    def _run_step(self, image) -> int:
        res = draw_rectangle_on_QR(image)

        if res == FAIL:
            text = "Please present your QR code"
        if res == SUCCESS:
            text = "Thank you for the QR Code"

        cv2.putText(image, text, (175, 30), cv2.FONT_HERSHEY_DUPLEX,
                    0.8, (195, 34, 34), 2, cv2.LINE_AA)

        if (res == SUCCESS):
            self.counter += 1
            if (self.counter > self.threshold):
                return BaseStep.SUCCESS
        else:
            self.counter = 0
        return BaseStep.RUNNING
