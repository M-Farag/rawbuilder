from faker import Faker


class Mocker:

    def __init__(self, size: int):
        """
        The Data Mocker object
        """
        self._size = size
        self._fake = Faker()

    def build(self, data_type):
        """
        Args:
            data_type(str|list): the mock type
        TODO:
            - support list mock types with extra features/filters EX: ["date", "between:(2010,2020)","min:(10)"]
        Returns:
            list
        """
        return self.__get_data_mock_function(data_type)()

    def __get_data_mock_function(self, data_type):
        """
        A dictionary lockup function to identify and execute the data mocker function

        Args:
            data_type(str|list): the mock type function name

        Returns:
            function object
        """
        all_data_generators_dict = {
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

        if data_type in all_data_generators_dict.keys():
            return all_data_generators_dict.get(data_type)
        return all_data_generators_dict.get('int')

    # D
    def __decrement(self):
        """
        Generate a list of decremented integers between the requested size and 1
        Returns:
            list
        """
        return list(range(self._size, 1, -1))

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
        return list(range(1, self._size, 1))

    # L
    def __last_name(self):
        """
        Generate a list of last names
        Returns:
            list

        """
        return [self._fake.last_name() for i in range(self._size)]
