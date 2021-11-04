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

    @property
    def schema(self):
        """
        The Schema as a property

        Returns:
            dictionary object
        """
        if self._schema is None:
            schema_path = pkg_resources.resource_filename(__name__, "../schema.yml")
            with open(schema_path) as file:
                self._schema = yaml.load(file, Loader=SafeLoader)
        return self._schema

    @property
    def schema_location(self):
        """
        The schema file location

        Returns:
            str
        """
        return 'Schema file location: {}'.format(pkg_resources.resource_filename(__name__, "../schema.yml"))
