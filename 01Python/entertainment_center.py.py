# -*- coding: utf-8 -*-

__author__ = 'dddd'

import media
import fresh_tomatoes



movie_list = [
    ('West World', 'Season 1',
     'https://images-na.ssl-images-amazon.com/images/M/MV5BMTEyODk5NTc2MjNeQTJeQWpwZ15BbWU4MDQ5NTgwOTkx._V1_SY1000_CR0,0,674,1000_AL_.jpg',
     'https://www.youtube.com/watch?v=IuS5huqOND4'),

     ('Game of Thrones', 'Season 6',
     'http://i1188.photobucket.com/albums/z418/yixing11940/Game%20of%20Thrones%20Season%20Six%20New%20Poster%2001%20.jpg',
     'https://www.youtube.com/watch?v=JxWfvtnHtS0'),

    ('Containment', 'Season 1',
     'https://s-media-cache-ak0.pinimg.com/736x/40/c8/cc/40c8cc3ccfd467612f04624e9038ae67.jpg',
     'https://www.youtube.com/watch?v=ASb4aL2nrEI'),

      ('Gone Girl', 'No words',
     'http://static1.1.sqspcdn.com/static/f/709071/26977244/1460978199853/Gone-Girl-aprilshowers-poster.jpg',
     'https://www.youtube.com/watch?v=2-_-1nJf8Vg'),

      ('Continuum', 'Season 4',
     'http://tvstock.net/sites/default/files/poster-continuum-season-4.jpg',
     'https://www.youtube.com/watch?v=3h0TjYS-sJ4'),

       ('Legend of the Seeker', 'Season 2',
     'http://vignette1.wikia.nocookie.net/sot/images/e/ee/Legend-of-the-seeker-poster.jpg',
     'https://www.youtube.com/watch?v=96OrBX1epXM'),
]

def makeMoveHtml(movie_info_list):
    movies = []
    for item in movie_list:
        movies.append(media.Movie(item[0], item[1], item[2], item[3]))

    fresh_tomatoes.open_movies_page(movies)


makeMoveHtml(movie_list)
print 'done'

# print media.__name__
#print media.__doc__
