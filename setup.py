from distutils.core import setup

setup(name='pytunes',
      version='0.2.3',
      description = 'A lightweight command-line music player',
      author = 'Eli Mullis',
      scripts=['pytunes.py', 'pytunes.conf', 'OptionParser.py', 'TrackQueue.py'])
