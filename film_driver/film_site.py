import re

from .film_base import FilmBase
from .phimmoi import PhimMoi
from .vungtv import VungTV


class FilmSite(FilmBase):

    domains = {
        'http://www.phimmoi.net': PhimMoi,
        'http://vungtv.com': VungTV,
    }

    def __init__(self, url):
        super().__init__()

        domain = ''

        m = re.search(r'http(s?)://([\w]+\.)+([\w]+)', url, re.IGNORECASE)
        if m is not None:
            domain = m.group(0).lower()

        for key, value in FilmSite.domains.items():
            if key == domain:
                self.__class__ = value

        self.fetch_url(url)

    def get_link(self):
        return []

    def get_playlist(self):
        return []
