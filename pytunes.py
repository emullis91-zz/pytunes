#!/usr/bin/env python
<<<<<<< HEAD
=======

>>>>>>> b28947640f9ef019643488c36bf1365e667ef9d9
'''
PyTunes is a Python script that queues and plays
music on the user's computer via the default system 
program that plays music files on the user's OS.

Version 0.2.2
Features:
Track queueing (one track or one album)
Track metadata output (artist, title, and album title)
Last.FM scrobbler
Shuffle

TODO:
multithreading/playback control
Lyrics searching/printing

'''
version = '0.2.2'
print "PyTunes Version %s" % version
print "Loading modules...."

'''Import modules and dependencies'''
from os import system
from time import time
import sys
import TrackQueue, getpass
import eyed3

def parse_opts(args):
    options = {}
    optcodes = [('a', 'album'), 
                ('r', 'shuffle'), 
                ('s', 'scrobble'),
                ('l', 'lyrics')]
    if args:
        for code, name in optcodes:
            options[name] = code in args[0]
    else:
        for code, name in optcodes:
            options[name] = False
    return options

def get_metadata(filepath):
    trackfile = eyed3.load(filepath)
    return (trackfile.tag.artist,
            trackfile.tag.title,
            trackfile.tag.album)
 
def main():

    tqueue = TrackQueue.TrackQueue()
    
    '''parse the first argument which is the 'artist - (album/track)' query'''
    artist_query = sys.argv[1].split('-')[0].strip()
    tracks_query = sys.argv[1].split('-')[1].strip()
    options = parse_opts(sys.argv[2:])

    if not options['album']:
        tqueue.queue_track(artist_query, tracks_query)
    else:    
        tqueue.queue_album(artist_query, tracks_query, options['shuffle'])

    if options['scrobble']:

        '''Import scrobbling dependencies'''
        import pylast

        try:
            API_KEY = '39164b1b13c9a1480a4266da5eb5b1b2'
            API_SECRET = '790d7e09963606149f61f625b1635f75'
            username = raw_input("Last.FM username: ")
            password = getpass.getpass("Last.FM password: ")
            NET = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET,
                  username = username, password_hash = pylast.md5(password))
            SESSION_KEY = pylast.SessionKeyGenerator(NET).get_session_key(username, pylast.md5(password))
            NET.session_key = SESSION_KEY
        
        #TODO: Improve exception handling
        except:
            print "An exception occurred."
            sys.exit()

    while not tqueue.empty():
        system('clear')
        track_path = tqueue.get()
        command = "afplay \"%s\"" % track_path
        artist, title, album = get_metadata(track_path)
        print "Now playing: \n%s\n%s\n%s" % (artist, title, album)
        system(command)
        
        if options['scrobble']:
            NET.scrobble(artist, title, int(time()))
        
        #if options['lyrics']:
        #TODO: Implement reliable lyrics scraping

if __name__ == '__main__':
    main()
