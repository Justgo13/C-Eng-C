import abc
import timeit
import cv2

"""
Link on how to install
https://pythonforundergradengineers.com/how-to-install-pytesseract.html
"""


class BaseStep:
    """
    A step used in the screening procedure
    """
    START = 0
    RUNNING = 1
    SUCCESS = 2
    FAIL = 3

    def __init__(self, name, description, timeout):
        """
        :param description The description of the step:
        :param timeout the maximum length of time the step should take before it fails in seconds:
        """
        self.start = 0
        self.name = name
        self.timeout = timeout
        self.description = description
        self.__status = BaseStep.START
        pass

    def run(self, image) -> int:
        """
        The run method is the one being called on by the main logic
        :param image the image from the camera:
        :return the status of the step:
        """
        runState = 0  # running status
        if self.__status == BaseStep.START:
            self.start = timeit.default_timer()
            pass
        runState = self._run_step(image)

        self.__status = return_val = BaseStep.FAIL if self._is_timeout() else runState

        if self.__status == BaseStep.FAIL or self.__status == BaseStep.SUCCESS:
            # reset the step to start again
            self.__status == BaseStep.START
            pass
        return return_val

    @abc.abstractmethod
    def _run_step(self, image) -> int:
        """
        Camera logic goes here for how the step works
        :param image the image to analyze:
        :return the status of how the step is going:
        """
        pass

    def _is_timeout(self) -> bool:
        """
        returns true if the step timed out
        :return true if the step timed out:
        """
        timeout = timeit.default_timer() - self.start >= self.timeout
        if timeout:
            self.reset()
            return True
        return False

    def reset(self):
        self.__status = BaseStep.START


    pass


class ExampleStep(BaseStep):

    def __init__(self, output):
        super().__init__("Example", "Example class to test", 3)
        self.output = output
        pass

    def _run_step(self, image) -> int:
        print(self.output)
        color = (255, 0, 0)
        end_point = (220, 220)
        start_point = (5, 5)
        thickness = 2
        image = cv2.rectangle(image, start_point, end_point, color, thickness)
        return ExampleStep.RUNNING

    pass
