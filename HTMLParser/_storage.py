"""
    Responsible for storing contents with related tags and also storing it as prompts

"""


class Storage:
    def __init__(self):
        self.raw_text = []
        self.prompt_text = []
        self.prompt_keys = []

    def append(self, raw_input: dict):
        self.raw_text.append(raw_input["content"])

        if raw_input["prompt"] is not None:
            prompt = f"[{raw_input['prompt']}] {raw_input['content']}"
            self.prompt_text.append(prompt)
            self.prompt_keys.append(prompt)

        else: 
            self.prompt_text.append(raw_input["content"])

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __str__(self):
        """
            Prints raw_text, prompt_text and prompt_keys seperated by \n\n\n
        """
        return "it will print this"


if __name__ == "__main__":
    # test run
    test_storage = Storage()
    print(test_storage)
    inputs = [
        {
            "prompt": "title",
            "content": "this is title",
        },
        {
            "prompt": None,
            "content": "this is a paragraph or something model will generate",
        },
        {
            "prompt": "subtitle",
            "content": "this is subtitle",
        },
        {
            "prompt": "Points",
            "content": "GPT model",
        }
    ]

    expected_raw_text = [
        "this is title",
        "this is a paragraph or something model will generate",
        "this is subtitle",
        "GPT model"
    ]

    expected_prompt_text = [
        "[TITLE] this is title",
        "this is a paragraph or something model will generate",
        "[SUBTITLE] this is subtitle",
        "[POINTS] GPT model"
    ]

    expected_prompt_key = [
        "[TITLE] this is title",
        "[SUBTITLE] this is subtitle",
        "[POINTS] GPT model"
    ]

    # running test
    for i in inputs:
        test_storage.append(i)

    print("Checking raw_text:", test_storage.raw_text == expected_raw_text)
    print("Checking prompt_text:", test_storage.raw_text == expected_prompt_text)
    print("Checking prompt_key:", test_storage.raw_text == expected_prompt_key)
