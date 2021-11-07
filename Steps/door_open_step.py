import cv2
from Steps.base_step import BaseStep
from face_mask_detection.face_detector import FaceMaskDetector


class DoorOpenStep(BaseStep):

    def __init__(self):
        super().__init__("Mask", "Ensure you are wearing a mask", 30)
        pass

    def _run_step(self, image) -> int:
        text = 'Welcome to Carleton. Door Unlocked'
        cv2.putText(image, text, (20, 30), cv2.FONT_HERSHEY_DUPLEX,
                    0.8, (30, 200, 30), 2, cv2.LINE_AA)

        return BaseStep.RUNNING