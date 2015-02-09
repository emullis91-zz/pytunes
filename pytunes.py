#!/usr/bin/env python
'''
PyTunes is a Python script that queues and plays
music on the user's computer via the default system 
program that plays music files on the user's OS.

Version 0.2.3
Features:
Track queueing (one track or one album)
Track metadata output (artist, title, and album title)
Last.FM scrobbler
Shuffle


TODO:
config parsing for metadata display
multithreading/playback control
lyrics scraping
'''

__version__ = '0.2.3'

print "PyTunes Version %s" % __version__
print "Loading modules...."

# Import modules and dependencies
from os import system
from time import time
import sys, platform
import eyed3, getpass
import TrackQueue as TQ
import OptionParser as OP
import ConfigParser as CP

# open program's config file for parsing as needed
conf = CP.ConfigParser()
conf.read("pytunes.conf")


'''Global variables include the OS family (OS X or Linux) 
   being used, and the system program used to play music 
   files (afplay or aplay).'''
if not conf.get('sys', 'player'):
    os_fam = platform.system()
    print "OS Detected: %s"
    if os_fam == "Darwin":
        sys_player = "afplay"
    elif os_fam == "Linux":
        sys_player = "mpg123"
else: 
    sys_player = conf.get('sys', 'player')
print sys_player

def get_metadata(filepath):
    # todo: read config file for track metadata
    # and related info.
    trackfile = eyed3.load(filepath)
    return (trackfile.tag.artist,
            trackfile.tag.title,
            trackfile.tag.album)
 

def main():

    tqueue = TQ.TrackQueue()

    all_options = ["album", "random", "scrobble"]
    oparse = OP.OptionParser(*all_options)
    oparse.set_defaults()

    if sys.argv[1][0] == "-":
        oparse.parse(sys.argv[1])
        artist_query = sys.argv[2].split('-')[0].strip()
        tracks_query = sys.argv[2].split('-')[1].strip()
    else:
        artist_query = sys.argv[1].split('-')[0].strip()
        tracks_query = sys.argv[1].split('-')[1].strip()

    if oparse.opt_map['a']:
        tqueue.queue_album(artist_query, tracks_query, oparse.opt_map['r'])
    else:
        tqueue.queue_track(artist_query, tracks_query)

    if oparse.opt_map['s']:
        # Import scrobbling dependencies
        import pylast

        API_KEY = conf.get('lastfm', 'API_KEY')
        API_SECRET = conf.get('lastfm', 'API_SECRET')
         
        username = conf.get('lastfm', 'user')
        password_hash = conf.get('lastfm', 'pass')

        if not username or not password_hash:
            username = raw_input("Last.FM username: ")
            password_hash = pylast.md5(getpass.getpass("Last.FM password: "))

        print "Logging user %s into Last.FM..." % username

        try:
            NET = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET,
                username = username, password_hash = password_hash)
            SESSION_KEY = pylast.SessionKeyGenerator(NET).get_session_key(
                username, password_hash)
            NET.session_key = SESSION_KEY
        
        except:
            print "An exception occurred."
            cont = ''
            while cont.lower() != 'y':
                cont = raw_input("Continue without scrobbling (y/n)? ")
                if cont.lower() == 'n':
                    sys.exit()

    while not tqueue.empty():
        system('clear')
        track_path = tqueue.get()
        print track_path
        command = "%s \"%s\"" % (sys_player, track_path)
        artist, title, album = get_metadata(track_path)
        print "Now playing: \n%s\n%s\n%s" % (artist, title, album)
        system(command)
        
        if oparse.opt_map['s']:
            NET.scrobble(artist, title, int(time()))
        
        #if options['lyrics']:
        #TODO: Implement reliable lyrics scraping

if __name__ == '__main__':
    main()
