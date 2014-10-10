#Song Picker
  
This is a song picking utility, for choosing a list of songs that within a certain total
duration.  For instance, if you go to the gym for an hour every day,
and want a different 60 minute playlist every time, this is
the tool for you!  P.S. I'm not a markdown expert so pleae no judging.  
  
##Getting the source:
Clone this repository!
  
##Installation:
I usually use pip + virtualenv for managing my installs.  Thus, you will find
a requirements.txt file, which you can use with  
`pip install -r requirements.txt`  
to install my dependencies!  Afterwords, just run  
`pip install file://<absolute path to package source>`  
  
##Usage:
`$ pick-songs -h
usage: pick-songs [-h] mp3_dir duration

positional arguments:
  mp3_dir     Path to a directory containing MP3 files, which must end in the
              .mp3 extension
  duration    The total duration the song list should approach, but not exceed

optional arguments:
  -h, --help  show this help message and exit`  
##Resources:
This package includes two files:        
1. song_picker.py:  A module containing the song-picking-library-goodies  
2. pick-songs: A command line utility for picking songs 
