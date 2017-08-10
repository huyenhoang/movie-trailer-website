import fresh_tomatoes
import media

# Create new instances of Movie for six movies, taking in their Name, Poster Image, and YouTuber Trailer #

great_gatsby = media.Movie("The Great Gatsby (1974)", "https://upload.wikimedia.org/wikipedia/en/f/fc/Great_gatsby_74.jpg", "https://www.youtube.com/watch?v=L-SGqutpxc0")

ferris_bueller = media.Movie("Ferris Bueller's Day Off", "https://upload.wikimedia.org/wikipedia/en/9/9b/Ferris_Bueller%27s_Day_Off.jpg", "https://www.youtube.com/watch?v=D6gABQFR94U")

holes = media.Movie("Holes", "https://upload.wikimedia.org/wikipedia/en/d/d6/Holesposter03.jpg", "https://www.youtube.com/watch?v=NEvLRtDKT0c")

good_will_hunting = media.Movie("Good Will Hunting", "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg", "https://www.youtube.com/watch?v=PaZVjZEFkRs")

king_speech = media.Movie("The King's Speech", "https://upload.wikimedia.org/wikipedia/en/a/a0/Kings_speech_ver3.jpg", "https://www.youtube.com/watch?v=R3okvbIlbQY")

passengers = media.Movie("Passenagers", "https://upload.wikimedia.org/wikipedia/en/8/8e/Passengers_2016_film_poster.jpg", "https://www.youtube.com/watch?v=7BWWWQzTpNU")

# The movies array contains a list of the movies to be displayed by the HTML code within fresh_tomatoes
movies = [great_gatsby, ferris_bueller, holes, good_will_hunting, king_speech, passengers]

fresh_tomatoes.open_movies_page(movies)


