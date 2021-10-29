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
