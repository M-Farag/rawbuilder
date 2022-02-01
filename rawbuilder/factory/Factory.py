from faker import Faker
import numpy as np


class Factory:

    def __init__(self, size: int):
        """
        The Data Mocker object
        """
        self._size = size
        self._fake = Faker()
        self._ranges = None

    def build_column(self, data_type: str):
        """
        Understand the data_type and build the column
        Args:
            data_type(str): the column data type and modifiers
        TODO:
            - Support complex column data types
        Returns:
            list
        """
        data_type_parts = data_type.strip().split(' ')

        for part in data_type_parts:
            """ Build ranges"""
            if part.startswith('between'):
                self._ranges = part.strip().split(',')
                self._ranges.remove('between')

        """Build column using the first data type part"""
        return self.__get_data_mock_function(data_type_parts[0])()

    def __get_data_mock_function(self, data_type):
        """
        A dictionary lockup function to identify and execute the data factory function

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
            # R
            "random_int": self.__random_int,
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
        return np.arange(start=self._size + 1, stop=1, step=-1)

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
            np.array
        """
        return np.arange(start=1, stop=self._size + 1, step=1)

    # L
    def __last_name(self):
        """
        Generate a list of last names
        Returns:
            list
        """
        return [self._fake.last_name() for i in range(self._size)]

    # S
    def __random_int(self):
        """
        Generate a list of random integers between two numbers

        Returns:
            list
        """
        rand_min, rand_max = 0, 100
        if self._ranges:
            rand_min,rand_max = min(self._ranges),max(self._ranges)

        return np.random.randint(rand_min, rand_max, size=self._size)
