"""
    Hugging face model loader
"""

from abc import ABC, abstractmethod


class BaseModelLoader(ABC):

    def __init__(self):

        self.model = self.load_model()
        self.tokenizer = self.load_tokenizer()
        self.pipeline = self.load_pipeline()

    @abstractmethod
    def load_model(self):
        ...

    @abstractmethod
    def load_tokenizer(self):
        ...

    @abstractmethod
    def load_pipeline(self):
        ...

    def generate(self, inputs: str, **kwargs):
        return self.pipeline(inputs, **kwargs)[0]["generated_text"]


if __name__ == "__main__":
    # test run
    ...