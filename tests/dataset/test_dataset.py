import pytest

import rawbuilder.dataset as rw


class TestInitDataObject(object):
    """with Good arguments"""

    def test_init_object_with_size_init_and_task_string_1(self):
        ds = rw.DataSet(10, 'task')
        assert isinstance(ds._config, dict)
        assert ds._config.get('size') == 10
        assert ds._config.get('task') == 'task'
        assert ds._schema is None
        assert ds._schema_location is None

    def test_init_rw_object_with_size_int_and_task_string_2(self):
        ds = rw.DataSet(1000000, 'user')
        assert isinstance(ds._config, dict)
        assert ds._config.get('size') == 1000000
        assert ds._config.get('task') == 'user'
        assert ds._schema is None
        assert ds._schema_location is None

    def test_init_rw_object_with_size_int_and_task_string_3(self):
        ds = rw.DataSet(10000, 'student')
        assert isinstance(ds._config, dict)
        assert ds._config.get('size') == 10000
        assert ds._config.get('task') == 'student'
        assert ds._schema is None
        assert ds._schema_location is None

    """bad arguments"""
    # @todo test for None values
    def test_init_rw_object_with_size_float_and_task_string(self):
        with pytest.raises(TypeError) as exception_info:
            ds = rw.DataSet(1.1, 'user')
        assert exception_info.match('Data set size must be an integer')

    def test_init_rw_object_with_size_string_and_task_string(self):
        with pytest.raises(TypeError) as exception_info:
            ds = rw.DataSet('text', 'user')
        assert exception_info.match('Data set size must be an integer')

    def test_init_rw_object_with_size_list_and_task_string(self):
        with pytest.raises(TypeError) as exception_info:
            ds = rw.DataSet(['size'], 'user')
        assert exception_info.match('Data set size must be an integer')

    def test_init_rw_object_with_size_int_and_task_int(self):
        with pytest.raises(TypeError) as exception_info:
            ds = rw.DataSet(10, 10)
        assert exception_info.match('Task name must be a string')

    def test_init_rw_object_with_size_int_and_task_float(self):
        with pytest.raises(TypeError) as exception_info:
            ds = rw.DataSet(10, 1.1)
        assert exception_info.match('Task name must be a string')

    def test_init_rw_object_with_size_int_and_task_list(self):
        with pytest.raises(TypeError) as exception_info:
            ds = rw.DataSet(10, [1.1])
        assert exception_info.match('Task name must be a string')