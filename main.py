#!/usr/bin/python3

from film_driver import FilmSite


def print_list(items):
    for item in items:
        print(item)


print('Phim Moi')
site = FilmSite('http://www.phimmoi.net/phim/boruto-naruto-the-he-ke-tiep-i1-4997/tap-7-119289.html')
print_list(site.get_link())
print_list(site.get_playlist())

print('-' * 50)

print('VungTV')
site = FilmSite('http://vungtv.com/phim/boruto-naruto-nhung-the-he-ke-tiep-boruto-naruto-next-generations-tap-7-26068')
print_list(site.get_link())
print_list(site.get_playlist())
