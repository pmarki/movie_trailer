class Movie:
    """Class stores information about particular movie: title, year,
    genre, storyline, poster image and youtube trailer"""

    def __init__(self, title, year, genre, storyline, poster, trailer):
        self.title = title
        self.year = year
        self.genre = genre
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
