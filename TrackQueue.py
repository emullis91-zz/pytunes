from Queue import Queue
from os import walk
from random import shuffle
from getpass import getuser
import re


music_dir = "/Users/%s/Music/" % getuser()

class TrackQueue(Queue, object):
    def __init__(self):
        super(TrackQueue, self).__init__()

    def queue_track(self, artist_query, song_query):
        searchpath = music_dir + artist_query
        for root, d, files in walk(searchpath):
            for track in files:
                if re.search(song_query, track, re.I): putpath = root + "/%s" % track
        self.put(putpath)


    def queue_album(self, artist_query, album_query, shuff = False):        
        searchpath = music_dir + "%s/%s" % (artist_query, album_query)
        for root, d, files in walk(searchpath):
            if shuff:
                shuffle(files)
            for track in files:
                if re.search('.mp3', track):
                    putpath = root + "/%s" % track
                    self.put(putpath)
