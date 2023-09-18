import requests
from HTMLParser._extractors import Extractor
from HTMLParser._key_config import medium_key_format


class HTMLParser:
    def __init__(self, page_link, language_specific=None):
        self.html_page = requests.get(page_link)
        print("gathered link resources")
        self.language_specific = language_specific
        self.extractor = Extractor(medium_key_format)

    def extract(self):
        return self.extractor.extract_content(self.html_page)

    def convertor(self, language):
        ...


if __name__ == "__main__":
    link = "https://medium.com/@cazad3011/my-google-interview-experience-d0377057243b"
    parser = HTMLParser(page_link=link)

    print(parser.extract())
