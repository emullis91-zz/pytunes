#!/usr/bin/python
import ConfigParser as CP

class OptionParser(object):
    def __init__(self, *options):
        self.all_options = options
        self.opt_map = {op[0]: False for op in self.all_options}

    def set_defaults(self):
        cf = CP.ConfigParser()
        cf.read('pytunes.conf')
        defaults = cf.get('sys', 'options')
        self.opt_map = {op[0]: op[0] in defaults for op in self.all_options} 

    def parse(self, args):
        for op in args[1:]:
            if not self.opt_map[op]:
                self.opt_map[op] = True
