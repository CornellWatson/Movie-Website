import media
import fresh_tomatoes

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



movies = [goonies, arrival, shawshank]

fresh_tomatoes.open_movies_page(movies)
