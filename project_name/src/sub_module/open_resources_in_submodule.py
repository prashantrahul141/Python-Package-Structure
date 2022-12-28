from importlib import resources
import io


def open_resource_from_submodule():
    '''use importlib.resource to open non .py files'''
    with resources.open_binary('project_name.resources.images', 'opensource.jpg') as fp:
        _resource_bytes = fp.read()
        resource = io.BytesIO(_resource_bytes)
        return resource
