==========
rawbuilder
==========


.. image:: https://img.shields.io/pypi/v/rawbuilder.svg
        :target: https://pypi.python.org/pypi/rawbuilder

.. image:: https://readthedocs.org/projects/rawbuilder/badge/?version=latest
        :target: https://rawbuilder.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




an elegant datasets factory


* Free software: MIT license
* Documentation: https://rawbuilder.readthedocs.io.



Features
========

* Schema oriented datasets builder

How to Use it
=================

Terminal:
::
    # Import the package into any python app
    import rawbuilder

    # Init the dataset object as ds
    ds = rawbuilder.DataSet(
        size=1000,
        task='user',
        schema_path='path/to/any/custom/json/schema'
    )

    # Build the dataset
    ds.build()

    # Get the schema location to edit with any IDE
    ds.schema_path

Schema
=================
- The Schema is a JSON object that describes three main components.
- The *model names*, the *column names*, and the *data types* per column.
- Note the below code-block, The model name is "Student", and it contain 4 properties [id,first_name,email,math_test_results].
- Each property of the model "student" is called a task and it has its columns and data source description.
- The builder will use all the information in the schema to build the required tasks or data sets.

Student data model example:
::
    "student": {
        "id": "int",
        "first_name": "first_name",
        "last_name": "last_name",
        "email": "email",
        "math_test_results": "random_int between,0,30"
    }

Data types to can use in the schema
************************************
- int: build a column of integers between 1 and requested dataset size.
- decrement: build a column of decremented integers between the requested size and 1.
- random_int: build a column of random integers between 0 and 100 by default.
- first_name: build a column of first names.
- last_name: build a column of last names.
- email: build a column of fake emails.

Data Modifiers
==============
Combine Data Modifiers to the above data types, it can adjust values, change the data nature, and gives more control over the final output.

Modifiers syntax is simple:
::
 "modifier,argument_1,arg_2,arg_*"

Use the modifier *between* to generate random integer column between 0 and 30:
::
 "math_test_results": "random_int between,0,30"

All Modifiers
*************

1) **Ranges**
--------------
Use this modifier to set the high-end and low-end for a specific data type

Syntax:
::
 "between,10,1000"

Supported with

random_int:
::
 "math_test_results": "random_int between,0,30"
