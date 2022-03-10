import pytest
from rawbuilder.factory import Factory
from faker import Faker


class TestInitFactoryObject(object):
    """Good arguments"""

    def test_init_factory_object_should_set_correct_properties(self):
        test_factory = Factory(size=10)
        assert test_factory._size == 10
        assert test_factory._ranges is None
        assert isinstance(test_factory._fake, Faker)

    """Bad arguments"""
    def test_init_factory_object_with_string_size_raise_value_error(self):
        with pytest.raises(TypeError) as exception_message:
            test_factory = Factory(size='1')
        assert exception_message.match('Size must be an integer')
