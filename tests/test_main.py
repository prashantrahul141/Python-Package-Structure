from io import BytesIO

from project_name.src.greetings import greetings
from project_name.src.importing_sub_modules import greetings_from_sub_module_through_main
from project_name.src.open_resources import open_resource


def test_greetings():
    '''
    use the convention 'test_function_name' to name
    your test functions.
    test only one function per test
    '''
    assert greetings("chief") == "Hello chief!"
    assert greetings("not chief") == "Hello not chief!"


def test_greetings_from_sub_module_through_main():
    '''
    testing functions imported from submodules
    in main module/file
    '''
    assert greetings_from_sub_module_through_main('chief') == 'Hello chief! from submodule using main module'
    assert greetings_from_sub_module_through_main('not chief') == 'Hello not chief! from submodule using main module'


def test_open_resource():
    '''
    testing resource load  function from main files.
    '''

    assert isinstance(open_resource(), BytesIO)
