from abc import ABC, abstractmethod
from ._storage import Storage


class BaseExtractor(ABC):
    def __init__(self, html_page):
        self.html_page = html_page
        self.storage = Storage()

    def _extract_keys(self):
        pass

    def _iterate_page(self, storage):
        pass

    @abstractmethod
    def remove_unwanted(self, page):
        pass

    def add_content(self, content):
        pass
