from faker import Faker


class Mocker:

    def __init__(self, size: int):
        """
        The Data Mocker object
        """
        self._size = size
        self._fake = Faker('en_CA')

    def build(self, mock_type):
        """

        Args:
            mock_type(str|list): the mock type

        Returns:
            list
        """
        return self.__get_data_mock_function(mock_type)

    def __get_data_mock_function(self, mock_type):
        """
        A dictionary lockup function to identify and execute the data mocker function

        Returns:
            function object
        """
        all_functions = {"first_name": self.__first_name,
                         "last_name": self.__last_name,
                         "email": self.__email,
                         "int": self.__int,
                         "decrement": self.__decrement}

        if mock_type in all_functions.keys():
            return all_functions.get(mock_type)()
        return all_functions.get('int')()

    def __int(self):
        return [i for i in range(1, self._size, 1)]

    def __decrement(self):
        return [i for i in range(self._size, 1, -1)]

    def __first_name(self):
        return [self._fake.first_name() for i in range(self._size)]

    def __last_name(self):
        return [self._fake.last_name() for i in range(self._size)]

    def __email(self):
        return [self._fake.email() for i in range(self._size)]
