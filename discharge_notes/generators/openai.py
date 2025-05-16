from openai import OpenAI

from discharge_notes.generators.base import BaseGenerator


class OpenAIGenerator(BaseGenerator):
    """
    OpenAI generator class.
    """

    def __init__(self, model: str = "gpt-4o", context: str = "", **model_kwargs):
        """
        Initialize the OpenAI generator.

        :param model: The OpenAI model to use.
        :param context: The context to use for the generator.
        :param model_kwargs: Additional keyword arguments for the model.

        Open AI API key is required to use this generator. Include it in the environment variable OPENAI_API_KEY.
        """
        self.model = model
        self.client = OpenAI()
        self.context = context
        self.model_kwargs = model_kwargs

    def generate(self, input_text) -> str:
        """
        Generate a response based on the input.

        :param input_text: The input text to generate a response for.
        :return: The generated response.
        """
        response = self.client.responses.create(
            model=self.model,
            instructions=self.context,
            input=input_text,
            **self.model_kwargs,
        )
        return response.output_text
