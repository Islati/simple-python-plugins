import pytest
import sys
import simpleplugins as plugins
from simpleplugins import Plugin, PluginManager


@pytest.fixture(scope="module")
def module():
    return plugins.import_module_from_file(sys.modules[__name__])


class TemplatePlugin(Plugin):
    def __init__(self, template_name, **kwargs):
        super(TemplatePlugin, self).__init__(**kwargs)
        self.template_name = template_name

    def activate(self):
        self.active = True
        print("Preparing template %s" % self.template_name)

    def deactivate(self):
        self.active = False
        print("Tearing down template %s" % self.template_name)

    def perform(self, **kwargs):
        print("Rendering template %s" % self.template_name)


class CookieCutterTemplate(TemplatePlugin):
    def __init__(self, template_name, url, **kwargs):
        super(CookieCutterTemplate, self).__init__(template_name, **kwargs)
        self.url = url

    def activate(self):
        super().activate()
        print("Cloning git repo %s" % self.url)

    def deactivate(self):
        super().deactivate()
        print("Removing template directory from git repo %s" % self.url)

    def perform(self, **kwargs):
        super().perform(**kwargs)
        print("Rendered Template %s" % self.url)


class YamlTemplate(TemplatePlugin):
    def __init__(self, template_name, data, **kwargs):
        super(YamlTemplate, self).__init__(template_name, **kwargs)
        self.data = data

    def activate(self):
        super().activate()
        print("Yaml data!")

    def deactivate(self):
        super().deactivate()
        print("No more yaml data!")

    def perform(self, **kwargs):
        super().perform(**kwargs)
        print("Rendered from Yaml!")


class ResolverConfigPlugin(YamlTemplate):
    def __init__(self, template_name, data, **kwargs):
        super(ResolverConfigPlugin, self).__init__(template_name, data, **kwargs)

    def activate(self):
        super().activate()

    def deactivate(self):
        super().deactivate()

    def perform(self, **kwargs):
        super().perform(**kwargs)


cookiecutter_commons_bukkitplugin = CookieCutterTemplate("cookiecutter-commons-bukkitplugin",
                                                         "https://github.com/TechnicalBro/cookiecutter-commons-bukkitplugin.git",
                                                         name="cookiecutter-commons-bukkitplugin")

cookiecutter_commons_minigame = CookieCutterTemplate("cookiecutter-commons-minigame",
                                                     "https://github.com/TechnicalBro/cookiecutter-commons-minigame.git",
                                                     name="cookiecutter-commons-minigame")
