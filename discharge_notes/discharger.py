import json

from discharge_notes.generators.base import BaseGenerator


class DischargeNoteBuilder:
    """
    Discharge note builder class.
    """

    def __init__(self, generator: BaseGenerator):
        """
        Initialize the discharge note builder.

        :param generator: The generator to use for generating the discharge note.
        """
        self.generator = generator

    def build_discharge_note(self, consultation_data: dict) -> dict:
        """
        Build a discharge note based on the consultation data.
        :param consultation_data: The consultation data to use for building the discharge note.
        :return: The generated discharge note.
        """

        note = self.generator.generate(json.dumps(consultation_data))
        return {"discharge_note": note}
