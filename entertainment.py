#!/usr/bin/env python


import media
import fresh_tomatoes

bahu = media.Movie("Bahubali The Conclusion", "war", "https://bit.ly/2GBNgc1",
                   "https://www.youtube.com/embed/sOEg_YZQsTI")
avengers = media.Movie("Avengers Infinity War", "war",
                       "https://bit.ly/2rnOhQx",
                       "https://bit.ly/2BxHO9t")
gang = media.Movie("Gang", "gang", "https://bit.ly/2IYFqP5",
                   "https://www.youtube.com/embed/vWD6kUP9RTY")
aaa = media.Movie("A Aa", "love", "https://bit.ly/2GzwQAZ",
                  "https://bit.ly/2IUgPuW")
master = media.Movie("The Drunken Master", "fight", "https://bit.ly/2ICFF2T",
                     "https://bit.ly/2Lj46jO")
movies = [bahu, avengers, gang, aaa]
fresh_tomatoes.open_movies_page(movies)
