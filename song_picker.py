"""Module for generating lists of songs.

The goal is to demonstrate my ability to write efficient code that
is as readable as possible.  While obsessing over performance is really
unecessary in this context, I wanted to show that I know how to
optimize my code to this level. This code adheres to PEP8, which is
why no line is longer than 72/79 characters (I'm still learning,
please be gentle with the PEP standards). As you can see, I'm also
using a few Google-Style docstrings.  I'm sure there are a couple
minor infractions, but I did run pylint for a 10/10 :)
"""
import os
import random


class Song(object):
    """Represents a song and its various meta attributes.

    I probably could have just used the class in eyed3,
    but by the time I pulled that library in this already existed.
    I also wanted to give an example of abstracting a data structure.
    """
    def __init__(self, title, artist, album, length, file_path):
        self._title = title
        self._artist = artist
        self._album = album
        self._length = length
        self._file_path = file_path

    def get_title(self):
        """Returns the title of this song"""
        return self._title

    def get_artist(self):
        """Returns the artist who created this song"""
        return self._artist

    def get_album(self):
        """Returns the album of this song"""
        return self._get_album

    def get_length(self):
        """Returns the length of this song, in seconds"""
        return self._length

    def get_file_path(self):
        """Returns the file path to this song"""
        return self._file_path

    @staticmethod
    def raise_if_no_eyed3():
        """Throws an environment error if eyed3 is unavailable"""
        if eyed3 == None:
            raise EnvironmentError("No eyed3 module is available")

    @classmethod
    def create_from_eyed3_file(cls, audio_file):
        """Given an eyed3 audiofile object, returns a Song object"""
        #We are doing this here so we throw a very clear import error
        #if eyed3 is unavailable, but only if someone is trying
        #to use functionality that depends on it
        #eyed3 is used to inspect MP3 files
        import eyed3

        if not isinstance(audio_file, eyed3.core.AudioFile):
            raise TypeError("You broke promises :(")

        return Song(
            audio_file.tag.title, audio_file.tag.artist, audio_file.tag.album,
            audio_file.info.time_secs, audio_file.path)

    @classmethod
    def create_from_mp3_path(cls, mp3_path):
        """Given a path to an mp3, returns a Song object"""
        import eyed3

        audio_file = eyed3.load(mp3_path)
        return cls.create_from_eyed3_file(audio_file)

    @classmethod
    def create_many_from_mp3_dir(cls, path_to_mp3_dir):
        """Given a path to a directory of MP3's, 
        returns a list of Song's.

        Args:
            path_to_mp3_dir (str): A path to a directory containing mp3
                files.  Each file must end with the .mp3 extension,
                and files that don't will be ignored.
        """
        songs = []
        dirty_mp3_paths = os.listdir(path_to_mp3_dir)
        clean_mp3_paths = [mp3_path for mp3_path in 
            dirty_mp3_paths if mp3_path.lower().endswith(".mp3")]

        if not clean_mp3_paths:
            raise EnvironmentError("No mp3's found in: %s" % path_to_mp3_dir)

        for mp3_path in clean_mp3_paths:
            songs.append(cls.create_from_mp3_path(mp3_path))

        return songs
                
class NoAvailableSongError(BaseException):
    """Thrown when no song that meets the specified criteria
    can be found
    """
    pass


class SongPicker(object):
    """Class that picks songs for you."""

    @classmethod
    def get_songs_for_duration(cls, max_duration, all_songs):
        """Get songs with total length not greater than max_duration.

        Will not modify or copy all_songs.  Avoids duplicate
        entries as much as possible i.e. the same song won't
        be returned in the chosen list twice, unless this is
        required to add duration.

        Args:
            max_duration (int): The maximum allowed duration of the
                returned song list.
            all_songs (list): A list of songs to build the
                subset from.

        Returns:
            list: A subset of all_songs that does not
                exceed max_duration.
        """
        song_subset = []
        current_duration = 0

        #Making a list of available song indexes allows us to
        #avoid randomly selecting songs that have already been chosen,
        #without copying all_songs, modifying it in place, or
        #iteratively guessing and throwing away results
        available_song_indexes = range(0, len(all_songs))

        while current_duration < max_duration:
            #If there are no more un-chosen song indexes,
            #reset the available indexes because we have done
            #are best not to choose a song more than once
            if len(available_song_indexes) == 0:
                available_song_indexes = range(0, len(all_songs))

            random_available_index = random.randrange(0, len(
                available_song_indexes))

            random_song_index = \
                available_song_indexes[random_available_index]

            #Remove the chosen available index,
            #So we don't select the same song more than once
            del available_song_indexes[random_available_index]

            random_song = all_songs[random_song_index]

            song_length = random_song.get_length()
            if current_duration + song_length > max_duration:
                remaining_duration = max_duration - current_duration

                try:
                    last_song = cls.get_last_song(
                        available_song_indexes, all_songs,
                        remaining_duration)
                    song_subset.append(last_song)
                except NoAvailableSongError:
                    #In real life this would log something instead,
                    #I promise I never ever catch exceptions
                    #without logging
                    print "Can not fit any more songs into total "\
                        "duration %d with %d currently remaining" % \
                        (max_duration, remaining_duration)

                return song_subset

            else:
                current_duration += song_length
                song_subset.append(random_song)

    @classmethod
    def get_last_song(
            cls, available_song_indexes,
            all_songs, remaining_duration):
        """Retrieves one last song from the all_songs list.

        Will choose the longest song that still fits in
        remaining_duration.
        """
        last_song = cls.get_longest_song_in_duration(
            available_song_indexes, all_songs,
            remaining_duration)

        if last_song == None:
            last_song = cls.get_longest_song_in_duration(
                range(0, len(all_songs)), all_songs,
                remaining_duration)

        if last_song == None:
            raise NoAvailableSongError("No songs exist that are \
                less than or equal to %d duration" % remaining_duration)

        return last_song

    @classmethod
    def get_longest_song_in_duration(
            cls, available_song_indexes, all_songs, remaining_duration):
        """Returns the longest song with a duration less than or equal
        to remaining_duration.

        Will attempt to choose from available_song_indexes first.
        """
        #Filter through the remaining available song indexes
        #Until the find the "Winning song", i.e. the one with
        #the longest duration that does not exceed our
        #remaining duration quota.
        current_winning_song = None
        current_winning_length = 0
        for available_index in available_song_indexes:
            this_song = all_songs[available_index]
            this_song_length = this_song.get_length()
            if not this_song_length > remaining_duration:
                if this_song_length > current_winning_length:
                    current_winning_song = this_song
                    current_winning_length = this_song_length
        return current_winning_song
