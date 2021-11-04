import pkg_resources
import yaml
from yaml.loader import SafeLoader


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
            boolean
        """
        schema_path = pkg_resources.resource_filename(__name__, "../schema.yml")
        with open(schema_path) as file:
            self._schema = yaml.load(file, Loader=SafeLoader)
            self._schema_location = schema_path
        return True
