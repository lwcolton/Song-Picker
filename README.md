#Song Picker Code Sample
  
Hi LeadPages!  This is my code sample package.  It's a song picking
utility, for choosing a list of songs that within a certain total
duration.  For instance, if you go to the gym for an hour every day,
and want a different 60 minute playlist every time, this is
the tool for you!  
  
##Installation:
I usually use pip + virtualenv for managing my installs.  Thus, you will find
a requirements.txt file, which you can use with  
`pip -r`  
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
  -h, --help  show this help message and exit
$
$ pick-songs ./ 60
Can not fit any more songs into total duration 60 with 1 currently remaining

Song 0
================
Title: Allegro from Duet in C Major
Artist: None
Length: 0`

##Resources:
This package includes two files:        
1. song_picker.py:  A module containing the song-picking-library-goodies
2. pick-songs: A command line utility for picking songs 
