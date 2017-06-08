#!/usr/bin/python3

from film_driver import FilmSite


def print_list(items):
    for item in items:
        print(item)


print('Phim Moi')
site = FilmSite('http://www.phimmoi.net/phim/boruto-naruto-the-he-ke-tiep-i1-4997/tap-7-119289.html')
print_list(site.get_link())
print_list(site.get_playlist())
