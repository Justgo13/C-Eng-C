from ScreeningStep import ScreeningStep


class AssessmentStep(ScreeningStep):

    def __init__(self):
        super.__init__("Self Test", "Scan your self test result", 15)
        pass

    def _run_step(self, image) -> int:
        return ScreeningStep.RUNNING
    pass

