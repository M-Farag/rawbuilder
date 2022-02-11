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
                                                                    "../{}".format(
                                                                        self._config.get('default_schema_file_name')))

            with open(self._schema_path) as file:
                self._schema = json.load(file)

        except FileNotFoundError:
            raise FileNotFoundError('Schema file not found')
        except ValueError:
            raise ValueError('Schema JSON is invalid')

    def build(self, export_csv=True, return_df=False):
        """
        Build the dataset

        Args:
            export_csv(bool): Return and write the dataset as a CSV file
            return_df(bool): Return the pandas dataframe after building it.

        Raises:
              ValueError: If the required task is not in the schema file
              ValueError: If the return_csv or return_df are not bool

        Returns:
              Pandas DataFrame (optional)
        """

        if not isinstance(export_csv, bool) or not isinstance(return_df, bool):
            raise ValueError('Arguments return_csv, return_df must of type bool')

        self._read_schema_file()

        if self._config.get('task') not in self.schema.keys():
            raise ValueError('Task: {} Not found in the schema file'.format(self._config.get('task')))

        task_breakdown = self.schema.get(self._config.get('task'))
        factory = Factory(self._config.get('size'))

        df = pd.DataFrame()
        for column_name, column_data_type in task_breakdown.items():
            df[column_name] = pd.Series(data=factory.build_column(column_data_type))

        output_file_name = '{}_{}.csv'.format(self._config.get('task'), self._config.get('size'))

        if export_csv:
            df.to_csv(output_file_name, chunksize=1000, index=False)
        print("File: {} was created successfully".format(output_file_name))

        del factory, task_breakdown

        if return_df:
            return df
        del df

