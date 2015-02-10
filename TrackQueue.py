from Queue import Queue
import ConfigParser as CP
from os import walk
from random import shuffle
import re

conf = CP.ConfigParser()
conf.read('pytunes.conf')

# music_dir in the conf file must be the full path to your
# music directory, with an ending forward slash.
music_dir = conf.get('sys', 'music_dir')

class TrackQueue(Queue, object):
    def __init__(self):
        super(TrackQueue, self).__init__()

    def queue_track(self, artist_query, song_query):
        searchpath = music_dir + artist_query
        for root, d, files in walk(searchpath):
            for track in files:
                if re.search(song_query, track, re.I): 
                    putpath = root + "/%s" % track
        self.put(putpath)


    def queue_album(self, artist_query, album_query, shuff = False):
        searchpath = music_dir + "%s/%s" % (artist_query, album_query)
        for root, d, files in walk(searchpath):
            if shuff:
                shuffle(files)
            else:
                files = sorted(files)
            for track in files:
                if re.search('.mp3', track):
                    putpath = root + "/%s" % track
                    self.put(putpath)
