import media
import fresh_tomatoes

# Objects of my favorite movies using the Movie class
goonies = media.Movie("The Goonies",
                      "http://spielbergfanclub.com/wp-content/uploads/2011/07/Goonies-poster.jpg",
                      "https://www.youtube.com/watch?v=hJ2j4oWdQtU"
                      )
arrival = media.Movie("The Arrival",
                      "http://t0.gstatic.com/images?q=tbn:ANd9GcSMztVicsYXcHHWNkejxIoFcW4H1eKhjSghAVixeAueuPEXmSKN",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g"
                      )

shawshank = media.Movie("Shawshank Redemption",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

napoleon = media.Movie("Napoleon Dynamite",
                       "http://www.gstatic.com/tv/thumb/movieposters/34617/p34617_p_v8_ab.jpg",
                       "https://www.youtube.com/watch?v=qH-FBPRf7NQ")


# List of my favorite movies
movies = [goonies, arrival, shawshank, napoleon]

# A method that displays my favorite movies using HTML & Bootstrap
fresh_tomatoes.open_movies_page(movies)
