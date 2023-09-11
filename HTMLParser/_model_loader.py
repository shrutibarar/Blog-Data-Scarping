"""
    Hugging face model loader
"""

from abc import ABC, abstractmethod
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain


class BaseModelLoader(ABC):

    def __init__(self, task):
        self.task = task

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, val: str):
        allowed_tasks = ["translate", "recognize"]

        if val not in allowed_tasks:
            raise ValueError(f"Expected task to be eiter {', '.join(allowed_tasks)}"
                             f"but got {val}")

        self._task = val

    @abstractmethod
    def load_model(self, model_key_or_id, **kwargs):
        ...

    @abstractmethod
    def load_tokenizer(self, **kwargs):
        ...

    @abstractmethod
    def load_pipeline(self, **kwargs):
        ...

    @abstractmethod
    def generate(self, inputs: str, **kwargs):
        ...


class OpenAIModelLoader(BaseModelLoader):
    def __init__(self, task: str, **kwargs):
        super().__init__(task)

        self.prompt = PromptTemplate.from_template(
            """
                You're a truthful assistant who {task} languages correctly else reply 'failed'
                
                {task} {add_task}: {sentence}
            """
        )

        self.model = self.load_model(**kwargs)
        self.pipeline = self.load_pipeline()

    def load_model(self, **kwargs):
        return ChatOpenAI(**kwargs)

    def load_tokenizer(self):
        return None

    def load_pipeline(self):
        return LLMChain(llm=self.model, prompt=self.prompt)

    def generate(self, inputs: dict, **kwargs):
        return self.pipeline.run(task=self.task, add_task=inputs["add_task"],
                                 sentence=inputs["sentence"])


if __name__ == "__main__":
    # test run
    from config import openai_key
    import os
    os.environ["OPENAI_API_KEY"] = openai_key
    llm = OpenAIModelLoader("translate")
    print(llm.generate(
        {
            "add_task": "to korean",
            "sentence": "I love you baby <3"
        }
    ))
