import pkg_resources
import yaml
from yaml.loader import SafeLoader
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
        self.read_schema()

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
        schema_path = pkg_resources.resource_filename(__name__, "../schema.yml")
        with open(schema_path) as file:
            self._schema = yaml.load(file, Loader=SafeLoader)
            self._schema_location = schema_path
        return True

    def build(self):
        """
        Build the dataset
        """
        self.__validate_tasks_exist_in_schema()

        for task_name in self._tasks:
            self.__build_task(self.schema.get(task_name))

        return True

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

    def __build_task(self, task_breakdown: dict):
        """
        Understand and Build all the requested tasks

        Args:
            task_breakdown(dict): The task breakdown as columns and data-sources
        Returns:
            Bool
        """
        print(task_breakdown)
