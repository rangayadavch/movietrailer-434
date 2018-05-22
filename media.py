#!/usr/bin/env python
import webbrowser


class Movie():
    '''
    class Movie():
    In this Class Movie set of attributes are declared to run
    movie trailer project.

    Attributes:
    attr1 (cineMax): Title of the movie.
    attr2 (cineLine): About the story line of the movie.
    attr3 (cinePostImage): Poster image of the movie.
    attr4 (cineTube): About youtube link  of the movie trailer.

    '''

    VALID_RATINGS = ["EXCELLENT", "GOOD", "BAD", "AVERAGE"]
    '''atr1,atr2,atr3,atr4'''

    def __init__(self, movie_title,
                 movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
