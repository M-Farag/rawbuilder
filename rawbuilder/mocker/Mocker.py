from faker import Faker


class Mocker:

    def __init__(self, size: int):
        """
        The Data Mocker object
        """
        self._size = size
        self._fake = Faker()

    def build(self, mock_type):
        """
        Args:
            mock_type(str|list): the mock type
        TODO:
            - support list mock types with extra features/filters EX: ["date", "between:(2010,2020)","min:(10)"]
        Returns:
            list
        """
        return self.__get_data_mock_function(mock_type)()

    def __get_data_mock_function(self, mock_type):
        """
        A dictionary lockup function to identify and execute the data mocker function

        Args:
            mock_type(str|list): the mock type function name

        Returns:
            function object
        """
        all_mock_types_generators_functions = {
            # D
            "decrement": self.__decrement,
            # E
            "email": self.__email,
            # F
            "first_name": self.__first_name,
            # I
            "int": self.__int,
            # L
            "last_name": self.__last_name,
        }

        if mock_type in all_mock_types_generators_functions.keys():
            return all_mock_types_generators_functions.get(mock_type)
        return all_mock_types_generators_functions.get('int')

    # D
    def __decrement(self):
        """
        Generate a list of decremented integers between the requested size and 1
        Returns:
            list
        """
        return [i for i in range(self._size, 1, -1)]

    # E
    def __email(self):
        """
        Generate a list of fake emails
        Returns:
            list
        """
        return [self._fake.email() for i in range(self._size)]

    # F
    def __first_name(self):
        """
        Generate a list of first names
        Returns:
            list

        """
        return [self._fake.first_name() for i in range(self._size)]

    # I
    def __int(self):
        """
        Generate a list of integers between 1 and requested size
        Returns:
            list
        """
        return [i for i in range(1, self._size, 1)]

    # L
    def __last_name(self):
        """
        Generate a list of last names
        Returns:
            list

        """
        return [self._fake.last_name() for i in range(self._size)]
