import requests
from bs4 import BeautifulSoup as _soup_


class Test:
    containers_thumb = []
    containers_title = []
    domains = []

    def __init__(self):
        self.start_reading()

    @classmethod
    def start_reading(cls):
        headers = {'User-Agent': 'Mozilla/5.0'}
        file_content = requests.get(url='https://old.reddit.com/r/Hololive/new/', headers=headers)
        flip_soup = _soup_(file_content, "html.parser")
        cls.containers_thumb = flip_soup.find_all('a', class_="thumbnail invisible-when-pinned may-blank loggedin ")
        cls.containers_title = flip_soup.find_all('a', class_="title may-blank loggedin ")
        cls.domains = flip_soup.find_all("span", class_="domain")
        '''https://www.datacamp.com/community/tutorials/scraping-reddit-python-scrapy'''
        print(cls.containers_title)
        for domain in cls.domains:
            if domain != "(self.datascience)":
                continue

            print(domain.text)

    @classmethod
    def update(cls):
        cls.start_reading()

    @classmethod
    def give_top(cls):
        return cls.containers_thumb[0], cls.containers_title[0]
