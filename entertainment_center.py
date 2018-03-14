import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "Toy Story is about the 'secret life of toys' when people are not around",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "8.3/10",
                        "G",
                        "1h 21min",
                        "Animation, Adventure, Comedy",
                        "(1995)")

avatar = media.Movie("Avatar",
                     "A paraplegic marine on a unique mission is dispatched to the moon Pandora",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "7.8/10",
                     "PG-13",
                     "2h 42min",
                     "Action, Adventure, Fantasy",
                     "(2009)")

fast_8 = media.Movie("The Fate of the Furious",
                     "A mysterious woman lures Dom and enthralled him to the state of betrayal",
                     "https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg",
                     "https://www.youtube.com/watch?v=uisBaTkQAEs",
                     "6.8/10",
                     "PG-13",
                     "2h 16min",
                     "Action, Adventure Crime",
                     "(2017)")

avengers_ultron = media.Movie("Avengers: Age of Ultron",
                              "Tony Stark creates the Ultron Program to protect the world",
                              "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
                              "https://www.youtube.com/watch?v=rD8lWtcgeyg",
                              "7.4/10",
                              "PG-13",
                              "2h 21min",
                              "Action, Adventure, Sci-fi",
                              "(2015)")

spiderman_homecoming = media.Movie("Spider-Man: Homecoming",
                                   "Peter Parker is exploring the concept of becoming an Avenger",
                                   "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                                   "https://www.youtube.com/watch?v=U0D3AOldjMU",
                                   "7.9/10",
                                   "PG-13",
                                   "2h 13min",
                                   "Action, Adventure, Sci-fi",
                                   "(2017)")

wonder_woman = media.Movie("Wonder Woman",
                           "Diana, princess of the Amazons, trained to be an unconquerable warrior.",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo",
                           "7.7/10",
                           "PG-13",
                           "2h 21min",
                           "Action, Adventure, Fantasy",
                           "(2017)")

movies = [toy_story, avatar, fast_8, avengers_ultron, spiderman_homecoming, wonder_woman]

fresh_tomatoes.open_movies_page(movies)
