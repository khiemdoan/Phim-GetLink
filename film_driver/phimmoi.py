from bs4 import BeautifulSoup
import requests
from .gibberish_aes import GibberishAES

from .film_base import FilmBase


class PhimMoi(FilmBase):

    def __init__(self):
        super().__init__()

    def get_link(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        script = soup.find('script', onload='checkEpisodeInfoLoaded(this)')
        src = script['src'].replace('javascript', 'json')
        episode_info = requests.get(src).json()
        videos = episode_info['medias']
        for video in videos:
            password = 'PhimMoi.Net@' + str(episode_info['episodeId'])
            video['url'] = GibberishAES(password).decrypt(video['url'])
        return videos

    def get_playlist(self):
        return []

