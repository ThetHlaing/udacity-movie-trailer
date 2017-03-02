import webbrowser

class Movie():
    """ This is the documentation of my class"""
    VALID_RATINGS = ["G","PG","PG-13","R"]
    def __init__(self,movie_title,storyline,poster_image,trailer_url,rating):
        self.title = movie_title
        self.storyline= storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url
        self.rating = rating
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
