from faker import Faker
import numpy as np


class Mocker:

    def __init__(self, size: int):
        """
        The Data Mocker object
        """
        self._size = size
        self._fake = Faker()
        self._simple_token = 'int'
        self._between_token = None

    def build(self, data_type_tokens):
        """
        Understand the data_type and build the column
        Args:
            data_type_tokens(str|list): the mock type
        TODO:
            - Support complex column data types
        Returns:
            list
        """
        token_matrix = [token.split(',') for token in data_type_tokens.strip().split(' ')]

        for row in token_matrix:
            if len(row) == 1:
                self._simple_token = row[0]
            if len(row) == 3 and 'between' in row:
                row.remove('between')
                self._between_token = row

        return self.__get_data_mock_function(self._simple_token)()

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
        return np.arange(start=self._size+1, stop=1, step=-1)

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
        return np.arange(start=1, stop=self._size+1, step=1)

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
        if self._between_token:
            rand_min = min(self._between_token)
            rand_max = max(self._between_token)

        return np.random.randint(rand_min, rand_max, size=self._size)
