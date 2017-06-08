import abc
import requests


class FilmBase(object, metaclass=abc.ABCMeta):

    def __init__(self):
        super().__init__()
        self.content = ''

    def fetch_url(self, url):
        self.content = requests.get(url).text

    @abc.abstractmethod
    def get_link(self):
        raise NotImplementedError("Please Implement this method")

    @abc.abstractmethod
    def get_playlist(self):
        raise NotImplementedError("Please Implement this method")
