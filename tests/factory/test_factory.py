import pytest
from rawbuilder.factory import Factory
from faker import Faker


class TestInitFactoryObject(object):
    """Good group"""

    def test_init_factory_object_should_set_correct_properties(self):
        test_factory = Factory(size=10)
        assert test_factory._size == 10
        assert test_factory._ranges is None
        assert isinstance(test_factory._faker, Faker)

    """Bad group"""

    def test_init_factory_object_with_string_size_raise_value_error(self):
        with pytest.raises(TypeError) as exception_message:
            test_factory = Factory(size='1')
        assert exception_message.match('Size must be an integer')


class TestSetDataModifiers(object):
    """ Good group"""

    def test_against_between_should_set_ranges(self):
        test_factory = Factory(size=1)
        test_factory._set_data_modifiers(['between,1,2'])
        assert isinstance(test_factory._ranges, list)
        assert len(test_factory._ranges) == 2

    def test_against_between_with_one_argument_should_set_ranges_as_one_input(self):
        test_factory = Factory(size=1)
        test_factory._set_data_modifiers(['between,1'])
        assert isinstance(test_factory._ranges, list)
        assert len(test_factory._ranges) == 1

    """Bad Group"""
    def test_with_non_list_should_raise_value_error(self):
        with pytest.raises(ValueError) as exception_message:
            test_factory = Factory(size=1)
            test_factory._set_data_modifiers('hello')
        assert exception_message.match('Column description parts must be a list')

    def test_with_any_data_modifier_without_arguments_should_raise_value_error(self):
        test_factory = Factory(size=1)
        with pytest.raises(ValueError) as exception_message:
            test_factory._set_data_modifiers(['hello'])
        assert exception_message.match('Any Data Modifier needs at least one argument')

    def test_against_between_without_arguments_should_raise_value_error(self):
        with pytest.raises(ValueError) as exception_message:
            test_factory = Factory(size=1)
            test_factory._set_data_modifiers(['between'])
        assert exception_message.match('Any Data Modifier needs at least one argument')
        assert test_factory._ranges is None
