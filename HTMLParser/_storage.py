"""
    Responsible for storing contents with related tags and also storing it as prompts

"""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Store:
    raw_text: List[str]
    prompt_text: List[str]
    prompt_keys: List[str]

    def get_text(self, separator: str = "=") -> str:
        combined_text = ""
        for i in self.__dict__:
            get_texts = "\n".join(self.__dict__[i])
            combined_text += f"{i}:\n{get_texts}\n{separator * 100}"
        return combined_text


class Storage:
    def __init__(self, separator="="):
        self.store = Store([], [], [])
        self.separator = separator

    def append(self, raw_input: Dict[str, str]):
        self.store.raw_text.append(raw_input["content"])

        if raw_input["prompt"] is not None:
            prompt = f"[{raw_input['prompt'].upper()}] {raw_input['content']}"
            self.store.prompt_text.append(prompt)
            self.store.prompt_keys.append(prompt)
        else: 
            self.store.prompt_text.append(raw_input["content"])

    def __repr__(self):
        return f"{self.__class__.__name__}(separator={self.separator})"

    def __str__(self):
        return self.store.get_text(separator=self.separator)
