#Song Picker Code Sample
  
Hi LeadPages!  This is my code sample package.  It's a song picking
utility, for choosing a list of songs that within a certain total
duration.  For instance, if you go to the gym for an hour every day,
and want a different 60 minute playlist every time, this is
the tool for you!
  
##Installation:
I usually use pip + virtualenv for managing my installs.  Thus, you will find
a requirements.txt file, which you can use with `pip -r` to install
my dependencies!  Afterwords, just run  
`pip install file://<absolute path to package source>`  
  
song_picker.py can be run directly from the command line, as 
`song_picker.py` on *nix and `python song_picker.py` on Windows.
You may also import the Song and SongPicker classes to leverage
the library in your own code.  I realize that in real life 
splitting the library and command-line tools into separate
files would be necessary, but, eh...
