import pytest
from simpleplugins import Plugin, PluginException, PluginManager


@pytest.fixture(scope="module")
def plugin_manager():
    return PluginManager()


@pytest.fixture(scope="module")
def base_plugin():
    return Plugin(name="Default Plugin", version="0.0.1")


@pytest.fixture(scope="module")
def clean_operation():
    return CleanOperation(name="clean_operation")


@pytest.fixture(scope="module")
def build_operation():
    return BuildOperation(name="build_operation")


@pytest.fixture(scope="module")
def operation_plugin():
    return OperationPlugin()


class OperationPlugin(Plugin):
    def __init__(self, **kwargs):
        super(OperationPlugin, self).__init__(**kwargs)

    def activate(self, **kwargs):
        self.active = True
        print("Activated Operation Plugin %s!" % self.name)

    def deactivate(self, **kwargs):
        self.active = False
        print("Deactivated Operation Plugin %s!" % self.name)

    def perform(self, **kwargs):
        print("Operation Performed on %s" % self.name)


class BuildOperation(OperationPlugin):
    def perform(self, **kwargs):
        super().perform(**kwargs)
        print("Built all plugins in App!")

    def deactivate(self, **kwargs):
        super().deactivate(**kwargs)
        print("Deactivated Builds Plugin")

    def activate(self, **kwargs):
        super().activate(**kwargs)
        print("Activated Builds Plugin")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CleanOperation(OperationPlugin):
    def __init__(self, **kwargs):
        super(CleanOperation, self).__init__(**kwargs)

    def activate(self, **kwargs):
        super().activate(**kwargs)

    def deactivate(self, **kwargs):
        super().deactivate(**kwargs)
        print("")

    def perform(self, **kwargs):
        super().perform(**kwargs)
        print("Cleaned all old plugin builds")
