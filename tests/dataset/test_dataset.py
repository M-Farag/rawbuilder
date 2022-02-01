import pytest

import rawbuilder.dataset as rw


class TestInitDataSetObject(object):
    """with Good arguments"""

    def test_init_object_with_size_init_and_task_string_1(self):
        ds = rw.DataSet(10, 'task')
        assert isinstance(ds._config, dict)
        assert ds._config.get('size') == 10
        assert ds._config.get('task') == 'task'
        assert ds._config.get('default_schema_file_name') == 'schema.json'
        assert ds._schema is None
        assert ds._schema_path is None

    def test_init_rw_object_with_size_int_and_task_string_2(self):
        ds = rw.DataSet(1000000, 'user')
        assert isinstance(ds._config, dict)
        assert ds._config.get('size') == 1000000
        assert ds._config.get('task') == 'user'
        assert ds._config.get('default_schema_file_name') == 'schema.json'
        assert ds._schema is None
        assert ds._schema_path is None

    def test_init_rw_object_with_size_int_and_task_string_3(self):
        ds = rw.DataSet(10000, 'student')
        assert isinstance(ds._config, dict)
        assert ds._config.get('size') == 10000
        assert ds._config.get('task') == 'student'
        assert ds._config.get('default_schema_file_name') == 'schema.json'
        assert ds._schema is None
        assert ds._schema_path is None

    def test_init_rw_object_with_schema_path_as_a_valid_string_as_path(self):
        ds = rw.DataSet(1, 'user', 'path/to/schema')
        assert ds._schema_path == 'path/to/schema'

    def test_init_rw_object_with_schema_path_as_none_object(self):
        ds = rw.DataSet(1, 'user')
        assert ds._schema_path is None

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


class TestReadSchema(object):

    @pytest.fixture
    def invalid_schema_file_fixture(self, tmpdir):
        invalid_file_path = tmpdir.join('invalid.json')
        with open(invalid_file_path, 'w') as file:
            file.write("hello world, not json data \n")
        yield invalid_file_path

    @pytest.fixture
    def valid_schema_file_fixture(self, tmpdir):
        valid_json_file_path = tmpdir.join('valid.json')
        with open(valid_json_file_path, 'w') as file:
            file.write('{"foo":"bar"}')
        yield valid_json_file_path

    """Bad group"""

    def test_read_schema_file_not_found_raise_file_not_found_error(self):
        with pytest.raises(FileNotFoundError) as exception_info:
            ds = rw.DataSet(1, 'user', 'anything.json')
            ds._read_schema_file()
        assert exception_info.match('Schema file not found')

    def test_read_schema_file_that_is_not_json_raise_value_error(self, invalid_schema_file_fixture):
        with pytest.raises(ValueError) as exception_info:
            ds = rw.DataSet(1, 'user', invalid_schema_file_fixture)
            ds._read_schema_file()
        assert exception_info.match('Schema JSON is invalid')

    """Good Arguments"""

    def test_read_schema_file_that_is_a_valid_json(self, valid_schema_file_fixture):
        ds = rw.DataSet(1, 'user', valid_schema_file_fixture)
        ds._read_schema_file()
        assert 'bar' == ds.schema['foo']
