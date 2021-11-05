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



=================
Features
=================

* Schema oriented datasets builder


=================
How to Use it
=================
.. code-block:: python

    # Import the package into any python app
    import rawbuilder

    # Init the dataset object as ds
    ds = rawbuilder.DataSet(
            size=1000,
            tasks=['user']
    )

    # Build the dataset
    ds.build()

=================
Credits
=================

This package was created with Cookiecutter_ .

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
