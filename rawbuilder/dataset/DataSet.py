import pkg_resources
import json
import pandas as pd
from ..factory.Factory import Factory


class DataSet:

    def __init__(self, size: int, task: str, schema_path=None):
        """
        DataSet object constructor

        Args:
            size (int): the maximum rows size per dataset
            task (list): List of datasets to be built
            schema_path (mixed): The path to an optional schema

        Raises:
            TypeError: when size is not int, task is not str
        Returns:
            object dataset
        """
        if not isinstance(size, int):
            raise TypeError('Data set size must be an integer')

        if not isinstance(task, str):
            raise TypeError('Task name must be a string')

        self._config = {'size': size, 'task': task, 'default_schema_file_name': 'schema.json'}
        self._schema, self._schema_path = None, schema_path

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
    def schema_path(self):
        """
        The schema file location

        Returns:
            str
        """
        self._read_schema_file()
        # @todo return from the config dict
        return self._schema_path

    def _read_schema_file(self):
        """
        Reading the schema file and init the schema  and the schema_location properties

        Returns:
            Bool
        """
        try:
            if self._schema_path is None:
                self._schema_path = pkg_resources.resource_filename(__name__,
                                                              "../{}".format(self._config.get('default_schema_file_name')))

            with open(self._schema_path) as file:
                self._schema = json.load(file)

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
