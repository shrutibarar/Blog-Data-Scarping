"""
    Hugging face model loader
"""


class ModelLoader:

    def __init__(self, model_id: str,
                 use_device="auto"):
        self.model_id = model_id
        self.use_device=use_device
        self.model = None
        self.tokenizer = None

    def load_mode(self):
        try:
            from transformers import AutoModel
        except ImportError:
            raise ImportError("transformers is not installed do 'pip install transformers'")
        return AutoModel.from_pretrained(self.model_id,
                                         use_device=self.use_device)

    def load_tokenizer(self, model_id):
        try:
            from transformers import AutoTokenizer
        except ImportError:
            raise ImportError("transformers is not installed do 'pip install transformers'")
        return AutoTokenizer.from_pretrained(model_id)

    def generate(self, inputs: str):
        ...
