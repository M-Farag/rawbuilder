import string

from faker import Faker
import numpy as np
import string


class Factory:

    def __init__(self, size: int):
        """
        The Data Mocker object
        """
        self._size = size
        self._fake = Faker()
        self._ranges = None

    def build_column(self, column_description: str):
        """
        Understand the data_type and build the column
        Args:
            column_description(str): the column data type and modifiers
        TODO:
            - Support complex column data types
        Returns:
            list
        """
        column_description_parts = column_description.strip().split(' ')

        # @todo check the number of parts must be >= 1
        if len(column_description_parts) < 1:
            raise KeyError('Column description must contain a data_type')

        column_data_type = column_description_parts.pop(0)

        self.__set_modifier_from_column_description_parts(column_description_parts)

        return self.__get_data_type_builder_method(column_data_type)()

    def __set_modifier_from_column_description_parts(self, column_description_parts: list):
        """
        Setting Modifiers from the column description parts
        User can pass multiple modifiers in the same line

        Args:
            column_description_parts:

        Returns:
            None

        """
        for part in column_description_parts:
            """ Build ranges"""
            if part.startswith('between'):
                self._ranges = part.strip().split(',')
                self._ranges.remove('between')

    def __get_data_type_builder_method(self, data_type):
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
            "random_float": self.__random_float,
            # S
            "password": self.__password,
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
        return np.arange(start=self._size, stop=0, step=-1)

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

    # R
    def __random_int(self):
        """
        Generate a list of random integers between two numbers

        Returns:
            np array
        """
        rand_min, rand_max = 0, 100
        if self._ranges:
            rand_min, rand_max = min(self._ranges), max(self._ranges)

        return np.random.randint(rand_min, rand_max, size=self._size)

    def __random_float(self):
        """
        Generate a list of random floats between two numbers

        Returns:
            np array
        """
        rand_min, rand_max = 0, 1
        if self._ranges:
            rand_min, rand_max = float(min(self._ranges)), float(max(self._ranges))

        return np.random.uniform(rand_min, rand_max, size=self._size).round(4)

    # P
    def __password(self):
        """
        Generate a password string

        Returns:
            str: the return value is a string
        """
        password_max_length = 12
        if self._ranges:
            password_max_length = max(self._ranges)
        return [self._fake.password(length=password_max_length) for i in range(self._size)]
