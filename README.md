pytunes is a music player that runs in the user's command line. It searches for songs in the user's music directory, queues them up, and then plays them in order using the OS X system program `afplay`.

####Dependencies
- [eyed3](http://eyed3.nicfit.net/)
- [pylast](https://code.google.com/p/pylast/) (Only needed for Last.FM scrobbling)

####Usage/Options
```
pytunes "[artist] - [title]" [options]
  -a    Queue all tracks from an album of the specified title; otherwise queue a single track with the specified title
  -s    Scrobble tracks to user's Last.FM profile (prompts user for username and password)
  -r    Shuffle album
```

####Future Additions
- Some form of playback control (pausing, skipping back/ahead)
- Ability to queue songs while playback is in progress
- Reliable lyrics scraping
- Linux compatibility
