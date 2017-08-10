# movie-trailer-website
View trailers of movies. This simple site is written using HTML, CSS, Bootstrap to displays the offical YouTube trailer for six movies that will bring you nostalgia from a Pyton class structure.

# Installation

Clone the GitHub repository to local drive.

Running the Python modules requires Python 2.7.9.

## Files

1. The file `media.py` contains the `class Movie` which takes four arguments: self, the title of the movie, the poster image, and the trailer link. The function `show_trailer` within this class opens the browser to the url of the movie trailer.

2. The Python module named 'fresh_tomatoes.py' contains function `open_movies_page()` which will take in the list of movies and generate an HTML file with the content and render a website with the list of movies.

3. The Python module named `entertainment.py` contains the list of instances of `class Movie`. 

## Launching the site

Run the `entertainment.py` module to launch the Movie Trailer Website. 

## Customization

This site can be customerized by modifying the arguments for `media.Movie()` in `entertainment.py` and by changing the HTML, CSS, logo image and social media links found in `fresh_tomatoes.py`.
