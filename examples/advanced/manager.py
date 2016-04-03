import os
from simpleplugins import PluginManager

plugin_manager = PluginManager()

# Register all the plugins found in the "plugins" folder, that exists along side the location of this file (manager.py)
plugin_manager.register(directory=os.path.abspath(os.path.join(os.path.dirname(__file__), "plugins")))

plugin_manager.register(plugin_file="myplugin.py")

from .plugins import MyOtherPlugin
plugin_manager.register(directory=os.path.abspath(os.path.join(os.path.dirname(__file__), "plugins")), skip_types=[MyOtherPlugin])
