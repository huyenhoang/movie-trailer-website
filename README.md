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

# Launching the site

## With Python IDLE

Run the `entertainment.py` module by double left-clicking the file or right click, then select 'Edit with IDLE', then 'Run', then 'Run Module'. This can also been accomplished by simply pressing F5.

## With Command Line

### On Mac

1. Create a folder with these files. Example `Project 1 - Movie Trailer Website`

2. Open Applications folder, go to Utilties, and open Terminal.

3. Type `cd` followed by the name of the folder created in step 1.

4. Type `python ./enterainment.py` to to launch the program.

### On Windows

1. Create a folder with these files. Example, `Project 1 - Movie Trailer Website`

2. In the Start menu, select "Run...", and type in `cmd`. This will cause the Windows terminal to open. Another way to do this is search for 'Command Prompt'.

3. Open the file `Project 1 - Movie Trailer Website` (or whatever you renamed it to). 

4. Type `cd C:\Desktop\Project 1 - Movie Trailer Website`

5. Type `entertainment.py` to launch the program.

### On Linux

1. Create a folder with these files. Example, `Project 1 - Movie Trailer Website`

2. Open up the Terminal. Make sure you know if you're in KDE or GNOME.

3. Type `cd ~/Project 1- Movie Trailer Website` to go into the folder created in step 1. Hit Enter.

4. Type `python ./entertainment.py` to launch the program.

# Customization

This site can be customerized by modifying the arguments for `media.Movie()` in `entertainment.py` and by changing the HTML, CSS, logo image and social media links found in `fresh_tomatoes.py`.
