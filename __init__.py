'''
Skeleton framework, from Eldorados urlresolver, to allow the inclusion of modules at runtime.
Outline the base class in plugnplay/interfaces.py
Plugins go in the plugins folder and should use a class outlined in plugnplay/interfaces.py
plugnplay.man.implementors(YourClass), will return a list of plugins that implement specified class
'''

import os
import plugnplay
from plugnplay.interfaces import PnPTest

plugnplay.set_plugin_dirs(os.getcwd() + '/pnpimporter/plugins/')
plugnplay.load_plugins()

print plugnplay.man.implementors(PnPTest)
