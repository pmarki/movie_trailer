import movie
import fresh_tomatoes

"""copy next line and fill in with your favourite movie details.
Take a look at samples provided. Then add it to move list below:
your_movie_title = movie.Movie("TITLE",
                      "YEAR",
                      "GENRE",
                      "STORYLINE",
                      "URL TO POSTER",
                      "URL TO YOUTUBE TRAILER")

"""

"""Let's create our favourites movies """
tytanic = movie.Movie("Tytanic",
                      "1997",
                      "drama, romance",
                      "A seventeen-year-old aristocrat falls in love \
                      with a kind, but poor artist aboard the \
                      luxurious, ill-fated R.M.S. Titanic.",
                      "http://ia.media-imdb.com/images/M/MV5BMjExNzM0NDM0N15BMl5BanBnXkFtZTcwMzkxOTUwNw@@._V1__SX1809_SY879_.jpg",
                # noqa
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

bodyguard = movie.Movie("Bodyguard",
                        "1992",
                        "drama, action, music",
                        "A former Secret Service agent takes on the job \
                        of bodyguard to a pop singer, whose lifestyle \
                        is most unlike a President's.",
                        "http://ia.media-imdb.com/images/M/MV5BMTYxMTc4NDc2N15BMl5BanBnXkFtZTYwNTYxMzA5._V1__SX1809_SY879_.jpg",
                # noqa
                         "https://www.youtube.com/watch?v=00Kvyw7AEKU")

avatar = movie.Movie("Avatar",
                     "2009",
                     "action, fantasy",
                     "A paraplegic marine dispatched to the moon Pandora \
                     on a unique mission becomes torn between \
                     following his orders and protecting the world.",
                     "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1__SX1809_SY879_.jpg",
                # noqa
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

the_girl = movie.Movie("The Girl with the Dragon Tattoo",
                       "2011",
                       "crime, drama",
                       "Journalist Mikael Blomkvist is aided in his search \
                       for a woman who has been missing for \
                       forty years by Lisbeth Salander, a young hacker.",
                       "http://ia.media-imdb.com/images/M/MV5BMTczNDk4NTQ0OV5BMl5BanBnXkFtZTcwNDAxMDgxNw@@._V1_SX214_AL_.jpg",
                # noqa
                       "https://www.youtube.com/watch?v=WVLvMg62RPA")

"""creating movie list as open_movies_pages requires list as a parameter"""
movies = [tytanic, bodyguard, avatar, the_girl]

"""generate webpage and show it"""
fresh_tomatoes.open_movies_page(movies)
