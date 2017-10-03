import pytest
from simpleplugins import Plugin
from ..fixtures.plugin_manager import OperationPlugin
from ..fixtures.plugin_module import YamlTemplate, TemplatePlugin


def test_plugin_manager(plugin_manager, base_plugin, clean_operation, build_operation, operation_plugin, module):
    plugin_manager.register(plugin=clean_operation)
    assert plugin_manager.has_plugin(name="clean_operation", plugin_type=clean_operation)

    plugin_manager.register(plugin=build_operation)
    assert plugin_manager.has_plugin(name="build_operation", plugin_type=build_operation)

    operations = plugin_manager.get_plugins(plugin_type=operation_plugin)
    assert len(operations) == 2

    for pl in operations:
        assert pl.active

    with pytest.raises(NotImplementedError) as ex_active:
        base_plugin.activate()

    assert 'not implemented' in str(ex_active.value)

    with pytest.raises(NotImplementedError) as ex_deactive:
        base_plugin.deactivate()

    assert 'not implemented' in str(ex_active.value)

    with pytest.raises(NotImplementedError) as ex_perform:
        base_plugin.perform()

    assert 'not implemented' in str(ex_perform.value)

    plugin_manager.unregister(clean_operation)

    assert plugin_manager.has_plugin(name="clean_operation") is False
    assert clean_operation.active is False

    plugin_manager.unregister(build_operation)

    assert plugin_manager.has_plugin(name="build_operation") is False
    assert build_operation.active is False

    plugin_manager.register(plugin_file=module, skip_types=[Plugin, OperationPlugin, TemplatePlugin, YamlTemplate])

    assert plugin_manager.has_plugin("cookiecutter-commons-minigame")
    assert plugin_manager.has_plugin("cookiecutter-commons-bukkitplugin")

    assert plugin_manager(name='cookiecutter-commons-minigame') is not None
    assert plugin_manager(plugin='cookiecutter-commons-minigame').name == 'cookiecutter-commons-minigame'
