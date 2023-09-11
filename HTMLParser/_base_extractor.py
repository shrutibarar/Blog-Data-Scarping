from _storage import Storage


class BaseExtractor:
    def __init__(self, storage):
        self.storage = storage

    def _extract_keys(self):
        pass

    def _iterate_page(self, storage):
        pass

    def remove_unwanted(self, page):
        pass

    def add_content(self, content):
        pass

