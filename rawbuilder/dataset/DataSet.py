import pkg_resources
import json
import pandas as pd
from ..mocker.Mocker import Mocker


class DataSet:

    def __init__(self, size: int, tasks: list):
        """
        DataSet object constructor

        Args:
            size (int): the maximum rows size per dataset
            tasks (list): List of datasets to be built

        Returns:
            object dataset
        """
        self._size = size
        self._tasks = tasks
        self._schema = None
        self._schema_location = None
        self._df = None

        # Config/Set schema and file location
        self.read_schema()
        # Config/Set data mocker object
        self._mocker = Mocker(self._size)

    @property
    def schema(self):
        """
        The Schema as a property

        Returns:
            dictionary object
        """
        if self._schema is None:
            self.read_schema()
        return self._schema

    @property
    def schema_location(self):
        """
        The schema file location

        Returns:
            str
        """
        if self._schema_location is None:
            self.read_schema()
        return self._schema_location

    def read_schema(self):
        """
        Reading the schema file and init the schema  and the schema_location properties

        Returns:
            Bool
        """
        schema_path = pkg_resources.resource_filename(__name__, "../schema.json")
        with open(schema_path) as file:
            self._schema = json.load(file)
            self._schema_location = schema_path
        return True

    def build(self):
        """
        Build the dataset
        """
        self.__validate_tasks_exist_in_schema()

        for task in self._tasks:
            self.__build_task(task, self.schema.get(task))

    def __validate_tasks_exist_in_schema(self):
        """
        Validate that all the required tasks are included in the schema

        Raises:
            ValueError(Exception): If the user provided a task that is not in the schema file

        Returns:
            Bool
        """

        for task in self._tasks:
            if task not in self.schema.keys():
                raise ValueError('Task: {} Not found in the schema file'.format(task))

        return True

    def __build_task(self, task_name: str, task_breakdown: dict):
        """
        Understand and Build all the requested tasks

        Args:
            task_breakdown(dict): The task breakdown as columns and data-sources
        Returns:
            Bool
        """
        self._df = pd.DataFrame()
        # iterate over task column names and mock_type
        for column_name, mock_type in task_breakdown.items():
            self._df[column_name] = pd.Series(data=self._mocker.build(mock_type))
        output_file_name = '{}_{}.csv'.format(task_name,self._size)
        self._df.to_csv(output_file_name, chunksize=100, index=False)
        self._df = None
        print("File: {} was created successfully".format(output_file_name))

