from ScreeningStep import ScreeningStep


class MaskStep(ScreeningStep):

    def __init__(self):
        super.__init__("Mask", "Ensure you are wearing a mask", 10)
        pass

    def _run_step(self, image) -> int:
        return ScreeningStep.RUNNING
    pass
