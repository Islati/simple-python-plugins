from simpleplugins import Plugin


class MyOtherPlugin(Plugin):
    def __init__(self):
        # Super Charge your plugin... With Inheritance!
        super(MyOtherPlugin, self).__init__()
        # Define your plugins name
        self.name = "MyOtherPlugin"
        # Define your plugins version (Optional, default is 1.0.0
        self.version = "1.0.0"
        # Define your plugins description (Optional, default is "No Description Available"
        self.description = "Another super awesome external plugin!!"

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

# Create the plugin instance, so it can be found when we scan & inspect.
my_plugin = MyOtherPlugin()
