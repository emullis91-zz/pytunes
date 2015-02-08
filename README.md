pytunes is a music player that runs in the user's command line. It searches for songs in 
the user's music directory, queues them up, and then plays them in order.

####Dependencies
- [eyed3](http://eyed3.nicfit.net/)
- [pylast](https://code.google.com/p/pylast/) (Only needed for Last.FM scrobbling)
- mpg123 (If you're running Linux; just install via your preferred package manager.)

####Usage and current options
```
pytunes -<options> "<artist> - <title>"
  -a    Queue all tracks from an album of the specified title; 
        otherwise queue a single track with the specified title
  -s    Scrobble tracks to user's Last.FM profile (prompts user for username and password)
  -r    Shuffle album
```

####Future Additions
- Queue control during playback
- Lyrics scraping
- More detailed and/or customizable metadata display
