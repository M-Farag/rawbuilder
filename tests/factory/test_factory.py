import pytest
from rawbuilder.factory import Factory
from faker import Faker

class TestInitFactoryObject(object):

    """Good arguments"""
    def test_init_factory_object_should_set_correct_properties(self):
        test_factory = Factory(size=10)
        assert test_factory._size == 10
        assert test_factory._ranges is None
        assert isinstance(test_factory._fake,Faker)


