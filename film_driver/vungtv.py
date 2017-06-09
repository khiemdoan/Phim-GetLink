from bs4 import BeautifulSoup
import requests
import re
import base64
import json

from .film_base import FilmBase


class VungTV(FilmBase):

    def __init__(self):
        super().__init__()

    def get_link(self):
        videos = []
        soup = BeautifulSoup(self.content, 'html.parser')
        script = soup.find('iframe')
        src = script['src']
        iframe = requests.get(src).text
        soup = BeautifulSoup(iframe, 'html.parser')
        scripts = soup.find_all('script')
        m = re.search(r'sources: \'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?\'', scripts[2].text)
        if m is not None:
            json_string = base64.b64decode(m.group(0)[10:-1]).decode('utf-8')
            videos = json.loads(json_string)
        m = re.search(r'hash: \'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?\'', scripts[2].text)
        if m is not None:
            json_string = base64.b64decode(m.group(0)[7:-1]).decode('utf-8')
            for video in json.loads(json_string):
                videos.append(video)
        return videos

    def get_playlist(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        episode_main = soup.find('div', {'class': 'episode-main'})
        episodes = episode_main.find_all('li')
        playlist = []
        for episode in episodes:
            playlist.append({
                'name': episode.find('a').text,
                'url': 'http://www.phimmoi.net/' + episode.find('a')['href'],
            })
        return playlist
