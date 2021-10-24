class DataSet:

    def __init__(self, size: int, schema: list, file_name: str):
        """
        DataSet object constructor

        Args:
            size (int): the maximum rows size per dataset
            schema (list): All the schemas that will build up the dataset
            file_name (str): The dataset output filename

        Returns:
            object dataset
        """
        self._size = size
        self._schema = schema
        self._file_name = file_name
