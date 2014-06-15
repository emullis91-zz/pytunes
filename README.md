pytunes is a music player that uses the unix `afplay` utility to queue and play music files on the user's hard drive.

####Dependencies
- [eyed3](http://eyed3.nicfit.net/)
- [pylast](https://code.google.com/p/pylast/) (Only needed for track scrobbling)

####Usage/Options
```
pytunes "[artist] - [title]" [options]
  -a    Queue all tracks from an album of the specified title; otherwise queue a single track with the specified title
  -s    Scrobble tracks to user's Last.FM profile (prompts user for username and password)
  -r    Shuffle album
  -l    Search for track lyrics and print if available
```
