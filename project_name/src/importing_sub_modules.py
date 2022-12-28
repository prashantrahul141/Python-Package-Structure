from project_name.src.sub_module.greetings_from_submodule import greetings_from_submodule


def greetings_from_sub_module_through_main(text: str = 'name'):
    '''importing functions and classes from sub modules'''
    _text = greetings_from_submodule(text)
    return _text + " using main module"
