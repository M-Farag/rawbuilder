import os.path

import pytest

import rawbuilder.dataset as rw


class TestInitDataSetObject(object):

    @pytest.fixture()
    def valid_schema_file_path_fixture(self, tmpdir):
        valid_file_path = tmpdir.join('schema.json')
        with open(valid_file_path, 'w') as file:
            file.write("hello world \n")
        yield valid_file_path

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

    def test_init_rw_object_with_schema_path_as_a_valid_string_as_path(self, valid_schema_file_path_fixture):
        ds = rw.DataSet(1, 'user', schema_path=valid_schema_file_path_fixture)
        assert ds._schema_path == valid_schema_file_path_fixture

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

    def test_init_rw_object_with_non_dict_schema_should_raise_type_error(self):
        with pytest.raises(TypeError) as exception_info:
            ds = rw.DataSet(1, 'user', schema_dict=[1, 2])
        assert exception_info.match('Schema_dict must be of type dictionary')

    def test_init_rw_object_with_invalid_schema_path_should_raise_File_exists_error(self):
        with pytest.raises(FileExistsError) as exception_info:
            ds = rw.DataSet(1, 'user', schema_path='/no/where/a.json')
        assert exception_info.match('Schema_path must be a file')


class TestReadSchemaFunction(object):

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

    def test_read_schema_file_not_found_raise_file_not_found_error(self, valid_schema_file_fixture):
        with pytest.raises(FileNotFoundError) as exception_info:
            ds = rw.DataSet(1, 'user', schema_path=valid_schema_file_fixture)
            ds._schema_path = '/no/files/at/all'
            ds._read_schema()
        assert exception_info.match('Schema file not found')

    def test_read_schema_file_that_is_not_json_raise_value_error(self, invalid_schema_file_fixture):
        with pytest.raises(ValueError) as exception_info:
            ds = rw.DataSet(1, 'user', invalid_schema_file_fixture)
            ds._read_schema()
        assert exception_info.match('Schema JSON is invalid')

    """Good Arguments"""

    def test_read_schema_file_that_is_a_valid_json(self, valid_schema_file_fixture):
        ds = rw.DataSet(1, 'user', valid_schema_file_fixture)
        ds._read_schema()
        assert 'bar' == ds.schema['foo']

    def test_read_schema_dict_is_a_valid_schema(self):
        test_schema_dict = {"task": "id"}
        ds = rw.DataSet(1, 'task', schema_dict=test_schema_dict)
        ds._read_schema()
        assert 'id' == ds.schema['task']


class TestBuildFunction(object):
    """Setup"""

    @pytest.fixture()
    def valid_schema_file_fixture(self, tmpdir):
        valid_file_path = tmpdir.join('schema.json')
        with open(valid_file_path, 'w') as file:
            file.write('{"task": {"id":"int"} }')
        yield valid_file_path

    """ Good group"""

    def test_build_without_path_and_dataset_size_will_create_a_file_with_expected_size(self, valid_schema_file_fixture):
        size = 2
        ds = rw.DataSet(size, 'task', valid_schema_file_fixture)
        ds.build()
        expected_file = 'task_{}.csv'.format(size)
        with open(expected_file, 'r') as file:
            assert file.readlines() == ['id\n', '1\n', '2\n']
        assert os.path.exists(expected_file)
        os.remove(expected_file)

    def test_build_with_defined_output_path_will_create_a_file_in_path(self, tmpdir, valid_schema_file_fixture):
        tmp_path = tmpdir.dirpath()
        ds = rw.DataSet(1, 'task', valid_schema_file_fixture)
        ds.build(output_path=tmp_path)
        expected_file = '{}/{}'.format(tmp_path, 'task_1.csv')
        assert os.path.exists(expected_file)

    def test_build_with_defined_path_and_dataset_size_will_create_a_file_with_expected_size(self, tmpdir,
                                                                                            valid_schema_file_fixture):
        tmp_path = tmpdir.dirpath()
        size = 2
        ds = rw.DataSet(size, 'task', valid_schema_file_fixture)
        ds.build(output_path=tmp_path)
        expected_file = '{}/task_{}.csv'.format(tmp_path, size)
        with open(expected_file, 'r') as file:
            assert file.readlines() == ['id\n', '1\n', '2\n']
        assert os.path.exists(expected_file)

    """Bad group"""

    def test_build_with_undefined_task_name_will_raise_value_error(self, valid_schema_file_fixture):
        with pytest.raises(ValueError) as exception_info:
            task_name = 'any_task'
            ds = rw.DataSet(100, task_name, valid_schema_file_fixture)
            ds.build()
        assert exception_info.match('Task: {} Not found in the schema file'.format(task_name))

    def test_build_with_non_boolean_return_csv_argument_raise_value_error(self, valid_schema_file_fixture):
        with pytest.raises(ValueError) as exception_info:
            ds = rw.DataSet(1, 'task', valid_schema_file_fixture)
            ds.build(export_csv=123)
        assert exception_info.match('Arguments return_csv, return_df must of type bool')
