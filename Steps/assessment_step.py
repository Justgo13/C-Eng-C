from Steps.base_step import BaseStep


class AssessmentStep(BaseStep):

    def __init__(self):
        super().__init__("Self Test", "Scan your self test result", 15)
        pass

    def _run_step(self, image) -> int:
        return BaseStep.RUNNING
    pass

