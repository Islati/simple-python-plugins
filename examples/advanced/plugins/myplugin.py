from simpleplugins import Plugin


class MyPlugin(Plugin):
    def __init__(self):
        # Super Charge your plugin... With Inheritance!
        super(MyPlugin, self).__init__()
        # Define your plugins name
        self.name = "MyPlugin"
        # Define your plugins version (Optional, default is 1.0.0
        self.version = "1.0.0"
        # Define your plugins description (Optional, default is "No Description Available"
        self.description = "Super awesome external plugin!!"

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

# Define the plugin so it can be found when performing a scan & inspection.
my_plugin = MyPlugin()
