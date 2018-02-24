# Copyright 2017 Kensho Technologies, Inc.
from setuptools import find_packages, setup

package_name = 'pytest-monkeytype'
version = '1.0.1'

# To update this pandoc --from=markdown --to=rst --output=README.rst README.md
long_description = """
pytest-monkeytype
=================

|Build Status| |License| |PyPI Python| |PyPI Version| |PyPI Status|
|PyPI Wheel|

`MonkeyType <https://github.com/Instagram/MonkeyType>`__ as a
`pytest <https://docs.pytest.org/en/latest/>`__ plugin.

::

    pip install pytest-monkeytype

    # Generate annotations by running your pytest tests as usual:
    py.test --monkeytype-output=./monkeytype.sqlite3

    # Get a listing of modules annotated by monkeytype
    monkeytype list-modules 

    # Generate a stub file for those annotations using monkeytype:
    monkeytype stub some.module

    # Apply these annotations directly
    monkeytype apply some.module

This project is inspired by
`pytest-annotate <https://github.com/kensho-technologies/pytest-annotate>`__

.. |Build Status| image:: https://travis-ci.org/mariusvniekerk/pytest-monkeytype.svg?branch=master
   :target: https://travis-ci.org/mariusvniekerk/pytest-monkeytype
.. |License| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0
.. |PyPI Python| image:: https://img.shields.io/pypi/pyversions/pytest-monkeytype.svg
   :target: https://pypi.python.org/pypi/pytest-monkeytype
.. |PyPI Version| image:: https://img.shields.io/pypi/v/pytest-monkeytype.svg
   :target: https://pypi.python.org/pypi/pytest-monkeytype
.. |PyPI Status| image:: https://img.shields.io/pypi/status/pytest-monkeytype.svg
   :target: https://pypi.python.org/pypi/pytest-monkeytype
.. |PyPI Wheel| image:: https://img.shields.io/pypi/wheel/pytest-monkeytype.svg
   :target: https://pypi.python.org/pypi/pytest-monkeytype

"""

setup(
    name=package_name,
    version=version,
    description='pytest-monkeytype: Generate Monkeytype annotations from your pytest tests.',
    long_description=long_description,
    url='',
    author='Marius van Niekerk',
    author_email='marius.v.niekerk@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'MonkeyType>=18.2.0',
        'pytest>=3.2.0'
    ],
    entry_points={
        'pytest11': [
            'pytest_monkeytype = pytest_monkeytype.plugin',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Framework :: Pytest',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing',
    ],
    keywords='pytest py.test types annotations MonkeyType monkeytype pep484',
    python_requires='>=3.6',
)
