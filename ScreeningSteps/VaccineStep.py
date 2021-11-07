from ScreeningStep import ScreeningStep


class VaccinePassportStep(ScreeningStep):

    def __init__(self):
        super.__init__("Vaccine Passport", "Scan the QR Code for your Proof of Vaccination", 15)
        pass

    def _run_step(self, image) -> int:
        return ScreeningStep.RUNNING
    pass
