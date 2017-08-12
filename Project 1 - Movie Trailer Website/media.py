# Importing the webbrowser allows the show_trailer function
# within the class Movie to open the web browser

import webbrowser

# This class takes 4 arguments:
# self, the movie's title, the poster image, and the YouTube Trailer link


class Movie():
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Opens the web browsers to the url of the movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
