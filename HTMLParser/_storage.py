"""
Module: _storage.py

This module provides classes for storing text content with related prompts

Classes:
    - Store: A container for raw text and prompt text
    - Storage: Manages content storage and retrieval

Usage Example:
    storage = Storage(separator="=")
    storage.append({"content": "This is some raw text.", "prompt": "Introduction"})
    print(storage)
"""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Store:
    """
        Store: A container for raw text and prompt text..

        Attributes:
             raw_text (List[str]): Stores raw text content.
             prompt_text (List[str]): Stores prompt text content.
             prompt_keys (List[str]): Stores keys associated with prompt text

        Methods:
             get_text(self, separator: str = "=") -> str:
             Combines raw and prompt text into a formatted st
    """
    raw_text: List[str]
    prompt_text: List[str]
    prompt_keys: List[str]

    def get_text(self, separator: str = "=") -> str:
        """
        Get formatted text combining raw and prompt text.

        Args:
            separator (str): The separator string to use. Default is "=".

        Returns:
            str: Formatted text combining raw and prompt text.
        """

        combined_text = ""
        for i in self.__dict__:
            get_texts = "\n".join(self.__dict__[i])
            combined_text += f"{i}:\n{get_texts}\n{separator * 100}"
        return combined_text


class Storage:
    """
    Storage: Manages content storage and retrieval.

    Attributes:
        store (Store): An instance of the Store class to manage content storage.
        separator (str): The separator string used in the formatted output. Default is "=".

    Methods:
        append(self, raw_input: Dict[str, str]):
            Appends content to storage, including raw and optional prompt text.
        __repr__(self):
            Returns a string representation of the Storage object.
        __str__(self):
            Returns a formatted string containing the stored content.

    Usage Example:
        storage = Storage(separator="=")
        storage.append({"content": "This is some raw text.", "prompt": "Introduction"})
        print(storage)
    """
    def __init__(self, separator="="):
        """
        Initialize a Storage instance.

        Args:
            separator (str): Separator string used in formatted output. Default is "="
        """
        self.store = Store([], [], [])
        self.separator = separator

    def append(self, raw_input: Dict[str, str]):
        """
        Append content to the storage.

        Args:
            raw_input (Dict[str, str]): A dictionary containing "content" and optional "prompt" keys.

        Example:
            storage.append({"content": "This is some raw text.", "prompt": "Introduction"})
        """
        self.store.raw_text.append(raw_input["content"])

        if raw_input["prompt"] is not None:
            prompt = f"[{raw_input['prompt'].upper()}] {raw_input['content']}"
            self.store.prompt_text.append(prompt)
            self.store.prompt_keys.append(prompt)
        else: 
            self.store.prompt_text.append(raw_input["content"])

    def __repr__(self):
        """
        Returns a string representation of the Storage object.

        Example:
            repr(storage)
        """
        return f"{self.__class__.__name__}(separator={self.separator})"

    def __str__(self):
        """
        Returns a formatted string containing the stored content.

        Example:
            print(storage)
        """
        return self.store.get_text(separator=self.separator)
