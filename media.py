import webbrowser


class Movie:
    __doc__ = """A class for story information about a movie"""

    def __init__(self, movie_title, movie_storyline, movie_year, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = movie_year

    def show_trailer(self):
        """Opens a web browser to the given url"""
        webbrowser.open(self.trailer_youtube_url)
