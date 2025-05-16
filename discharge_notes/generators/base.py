from abc import ABC
from abc import abstractmethod


class BaseGenerator(ABC):
    """
    Base class for all generators.
    """

    @abstractmethod
    def generate(self, input_text) -> str:
        """
        Generate a response based on the input.
        """
        pass
