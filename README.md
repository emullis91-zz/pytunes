pytunes is a music player that runs in the user's command line. It uses one of two system programs (`aplay` for Linux, `afplay` for OS X) to play files after queueing them from the user's music directory tree.

####Dependencies
- [eyed3](http://eyed3.nicfit.net/)
- [pylast](https://code.google.com/p/pylast/) (Only needed for Last.FM scrobbling)

####Usage/Options
```
pytunes "[artist] - [title]" [options]
  -a    Queue all tracks from an album of the specified title; otherwise queue a single track with the specified title
  -s    Scrobble tracks to user's Last.FM profile (prompts user for username and password)
  -r    Shuffle album
  -l    Search for track lyrics and print if available
```
