#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['pandas', 'faker', 'numpy']

test_requirements = ['pytest>=3', ]

setup(
    author="Mina Farag Amin",
    author_email='mina.farag@icloud.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="an elegant datasets factory",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='rawbuilder',
    name='rawbuilder',
    packages=find_packages(include=['rawbuilder', 'rawbuilder.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/M-Farag/rawbuilder',
    version='0.0.6',
    zip_safe=False,
    package_data={"": ["*.json"]},
)
