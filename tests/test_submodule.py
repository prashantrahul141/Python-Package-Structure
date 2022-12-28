from io import BytesIO

from project_name.src.sub_module.greetings_from_submodule import greetings_from_submodule
from project_name.src.sub_module.open_resources_in_submodule import open_resource_from_submodule


def test_greetings_from_submodule():
    '''
    testing sub module functions
    '''
    assert greetings_from_submodule("chief") == "Hello chief! from submodule"
    assert greetings_from_submodule("not chief") == "Hello not chief! from submodule"


def test_open_resource_from_submodule():
    '''
    testing sub module's resource load function
    '''
    assert isinstance(open_resource_from_submodule(), BytesIO)
