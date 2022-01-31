import pkg_resources
import json
import pandas as pd
from ..factory.Factory import Factory


class DataSet:

    def __init__(self, size: int, task: str):
        """
        DataSet object constructor

        Args:
            size (int): the maximum rows size per dataset
            task (list): List of datasets to be built
        Raises:
            TypeError: when size is not int, task is not str
        Returns:
            object dataset
        """
        if not isinstance(size, int):
            raise TypeError('Data set size must be an integer')

        if not isinstance(task, str):
            raise TypeError('Task name must be a string')

        self._config = {'size': size, 'task': task, 'schema_file_name': 'schema.json'}
        # @todo move schema & schema_location to the config dict
        self._schema, self._schema_location = None, None

    @property
    def schema(self):
        """
        The Schema as a property

        Returns:
            dictionary object
        """
        self._read_schema_file()
        # @todo return from the config dict
        return self._schema

    @property
    def schema_location(self):
        """
        The schema file location

        Returns:
            str
        """
        self._read_schema_file()
        # @todo return from the config dict
        return self._schema_location

    def _read_schema_file(self, schema_path=None):
        """
        Reading the schema file and init the schema  and the schema_location properties

        Returns:
            Bool
        """
        try:
            if schema_path is None:
                schema_path = pkg_resources.resource_filename(__name__, "../{}".format(self._config.get('schema_file_name')))

            with open(schema_path) as file:
                self._schema = json.load(file)
                self._schema_location = schema_path
        except FileNotFoundError:
            raise FileNotFoundError('Schema file not found')
        except ValueError:
            raise ValueError('Schema JSON is invalid')

    def build(self):
        """
        Build the dataset
        """

        self._read_schema_file()

        if self._config.get('task') not in self.schema.keys():
            raise ValueError('Task: {} Not found in the schema file'.format(self._config.get('task')))

        task_breakdown = self.schema.get(self._config.get('task'))
        factory = Factory(self._config.get('size'))

        df = pd.DataFrame()
        for column_name, column_data_type in task_breakdown.items():
            df[column_name] = pd.Series(data=factory.build_column(column_data_type))

        output_file_name = '{}_{}.csv'.format(self._config.get('task'), self._config.get('size'))
        df.to_csv(output_file_name, chunksize=1000, index=False)
        del df, factory, task_breakdown

        print("File: {} was created successfully".format(output_file_name))
