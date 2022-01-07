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

        Returns:
            object dataset
        """
        self._config = {'size': size, 'task': task}
        self._schema, self._schema_location = None, None

    @property
    def schema(self):
        """
        The Schema as a property

        Returns:
            dictionary object
        """
        self.__read_schema()
        return self._schema

    @property
    def schema_location(self):
        """
        The schema file location

        Returns:
            str
        """
        self.__read_schema()
        return self._schema_location

    def __read_schema(self):
        """
        Reading the schema file and init the schema  and the schema_location properties

        Returns:
            Bool
        """
        schema_path = pkg_resources.resource_filename(__name__, "../schema.json")
        with open(schema_path) as file:
            self._schema = json.load(file)
            self._schema_location = schema_path

    def build(self):
        """
        Build the dataset
        """

        # Config/Set schema and file location
        self.__read_schema()

        if self._config['task'] not in self.schema.keys():
            raise ValueError('Task: {} Not found in the schema file'.format(self._config['task']))

        # Task break down columns & data_types
        task_breakdown = self.schema.get(self._config['task'])

        # Init Empty Pandas DataFrame
        df = pd.DataFrame()

        # Config/Set data factory object
        factory = Factory(self._config['size'])

        # Iterate over task column names and data_type
        # Feature engineering the DataSet
        for column_name, data_type in task_breakdown.items():
            df[column_name] = pd.Series(data=factory.build_column(data_type))

        # Saving the file
        output_file_name = '{}_{}.csv'.format(self._config['task'], self._config['size'])
        df.to_csv(output_file_name, chunksize=1000, index=False)
        del df, factory, task_breakdown

        # Acknowledgement
        print("File: {} was created successfully".format(output_file_name))
