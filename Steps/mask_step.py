import cv2
from Steps.base_step import BaseStep
from face_mask_detection.face_detector import FaceMaskDetector


class MaskStep(BaseStep):

    def __init__(self):
        super().__init__("Mask", "Ensure you are wearing a mask", 30)
        self.model = FaceMaskDetector()
        self.counter = 0
        self.threshold = 30
        pass

    def _run_step(self, image) -> int:
        res, image = self.model.detect_face(image)

        if res == 'neither':
            text = 'Welcome to Carleton'
        if res == 'no_mask':
            text = "Please wear your mask"
        if res == 'mask':
            text = 'Thank you for your mask'

        cv2.putText(image, text, (175, 30), cv2.FONT_HERSHEY_DUPLEX,
                    0.8, (195, 34, 34), 2, cv2.LINE_AA)

        if (res == 'mask'):
            self.counter += 1
            if (self.counter > self.threshold):
                return BaseStep.SUCCESS
        else:
            self.counter = 0
        print(self.counter)
        return BaseStep.RUNNING
