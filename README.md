**Dead-Simple Python Plugins**
--------------------------------

***Introducing Simple Python Plugins***

With a project that could truly benefit from a plugin system, it's a shame that existing solutions are esoteric and have an unworthy amount of overhead for something so simple.

*That changes **now**.*

### Getting Started ###

    # Import the PluginManager, and Plugin class!
    from simpleplugins import Plugin, PluginManager
    
    # Create your Plugin Manager!
    plugin_manager = PluginManager()
    
    # Create your very first plugin!
    class MyPlugin(Plugin):
        def __init__(self):
	        # Required call to Plugin
            super(MyPlugin, self).__init__()
            # Define your plugins name
            self.name = "MyPlugin"
            # Define your plugins version (Optional, default is 1.0.0
            self.version = "1.0.0"
            # Define your plugins description (Optional, default is "No Description Available"
            self.description = "Super awesome example plugin!"
    
        def activate(self):
            # Define operations to perform when your plugin is activated!
            print("%s has been activated!" % self.name)
    
        def deactivate(self):
            # Define operations to perform when your plugin is deactivated
            print("%s has been deactivated!" % self.name)
    
        def perform(self, **kwargs):
            # Define the operations that will be executed when "performing" the plugin.
            # This is where the main functionality of the plugin will reside.
    
            print("Preparing to perform an extremely complex task with '%s'" % self.name)
            # ....
            print("Complex Operation Complete!")
    
    # Create an instance of your plugin!
    plugin = MyPlugin()
    
    # Register the plugin!
    plugin_manager.register(plugin)
    
    # Now retrieve, and perform!
    plugin_manager.get_plugin("MyPlugin").perform()
    
#### Advanced Example

While the above example is basic, and very straight-forward, it takes very little effort to get some extreme power from this library.

*To view an example displaying all advanced features, click here.*

***Here's a quick preview of what's possible.***
 
*Scan a directory for modules containing plugins, and register them.*

    # The code below should assure the absolute path of 
    # "plugins_dir", as opposed to simply passing the
    # folder name. For sake of simplicity this is 
    # excluded in the example
    
	plugin_manager.register(directory="plugins_dir")

*Register plugins through the path of an individual module.*

    plugin_manager.register(plugin_file="myplugin.py")

*Skip the registration of plugins matching a specific type*

	# The code below should assure the absolute path of 
    # "plugins_dir", as opposed to simply passing the
    # folder name. For sake of simplicity this is 
    # excluded in the example
	
	from .plugins import MyOtherPlugin

	plugin_manager.register(directory="plugins", skip_types=[MyOtherPlugin])

 *Delay activation of plugins until you choose to activate them*
 

    plugin_manager.register(directory="plugins",activate=False)