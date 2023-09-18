from typing import Dict


class KeyExtractor:
    def __init__(self, contents_format_keys: Dict):
        self.contents_format_keys = contents_format_keys

    def _create_prompt(self, tag: str, content: str, all_class_element: list):
        prompts = {
            "prompt": None,
            "content": content,
        }

        class_element = None
        for key, val in self.contents_format_keys[tag].items():
            if key in " ".join(all_class_element):
                class_element = key
                break

        if class_element is None:
            return prompts

        prompts["prompt"] = self.contents_format_keys[tag][class_element]

        return prompts

    def extract(self, data):
        # do something for images and links
        if data["tag"] not in self.contents_format_keys:
            return None
        return self._create_prompt(data["tag"], data["content"], data["class"])
