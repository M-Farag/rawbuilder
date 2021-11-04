class Mocker:

    def __init__(self):
        """
        The Data Mocker object
        """

    def build(self, size: int, mock_type):
        """

        Args:
            mock_type(str|list): the mock type
            size(int): the maximum rows number

        Returns:
            list
        """
        return [i for i in range(size)]

