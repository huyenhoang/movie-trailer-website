# movie-trailer-website
View trailers of movies. This simple site is written using HTML, CSS, Bootstrap to displays the offical YouTube trailer for six movies that will bring you nostalgia from a Pyton class structure.

# Installation

Clone the GitHub repository to local drive.

Running the Python modules requires Python 2.7.9.

## On Mac
To determine if you have Python 2.7, open the Terminal application, type the following, and press Return:

`python -V`

This command will report the version of Python:

`Python 2.7.9`

Any version between 2.7.0 and 2.7.10 is fine.

## On Windows 7

To get to the command line, open the Windows menu and type “command” in the search bar. Select Command Prompt from the search results.

In the Command Prompt window, type the following and press Enter.

`python`

If Python is installed and in your path, then this command will run python.exe and show you the version number.

`Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.`

Otherwise, you will see:

`'python' is not recognized as an internal or external command, operable program or batch file.`

## On Linux

Open a shell and type

`which python`

If Python is installed, you will get back its location, which may or may not include the version number. If the location does not include a version number, then ask for it:

`python -V`

This command returns the version

`Python 2.7.9`

# Files

1. The file `media.py` contains the `class Movie` which takes four arguments: self, the title of the movie, the poster image, and the trailer link. The function `show_trailer` within this class opens the browser to the url of the movie trailer.

2. The Python module named 'fresh_tomatoes.py' contains function `open_movies_page()` which will take in the list of movies and generate an HTML file with the content and render a website with the list of movies.

3. The Python module named `entertainment.py` contains the list of instances of `class Movie`. 

## Launching the site

Run the `entertainment.py` module by double left-clicking the file or right click, then select 'Edit with IDLE', then 'Run', then 'Run Module'. This can also been accomplished by simply pressing F5.

# Customization

This site can be customerized by modifying the arguments for `media.Movie()` in `entertainment.py` and by changing the HTML, CSS, logo image and social media links found in `fresh_tomatoes.py`.
