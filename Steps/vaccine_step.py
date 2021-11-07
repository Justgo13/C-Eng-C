from Steps.base_step import BaseStep


class VaccinePassportStep(BaseStep):

    def __init__(self):
        super().__init__("Vaccine Passport", "Scan the QR Code for your Proof of Vaccination", 15)
        pass

    def _run_step(self, image) -> int:
        return BaseStep.RUNNING
    pass
