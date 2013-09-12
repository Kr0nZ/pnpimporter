import pnpimporter
from pnpimporter.plugnplay import Interface
import sys


class PnPTest(Interface):
    
    name = 'override_me'
    '''(str) A human readable name for your plugin.'''

    priority = 100
    '''
    (int) The order in which plugins will be tried. Lower numbers are tried 
    first.
    '''    
