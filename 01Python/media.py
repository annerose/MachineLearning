# -*- coding: utf-8 -*-
"""Class for movie info."""
__author__ = 'dddd'



class Movie( ):
    """
    movi info class
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ class Movie's contructor
        :param movie_title: title string
        :param movie_storyline:storyline string
        :param poster_image: image_url string
        :param trailer_youtube: youtube_url_string
        :return: Movie object
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # discard
    # def show_trailer(self):
    #     webbrowser.open(self.trailer_youtube_url)