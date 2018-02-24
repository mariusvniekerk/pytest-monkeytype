# Copyright 2017 Kensho Technologies, Inc.
from setuptools import find_packages, setup

package_name = 'pytest-monkeytype'
version = '1.0.0'

setup(
    name=package_name,
    version=version,
    description='pytest-monkeytype: Generate Monkeytype annotations from your pytest tests.',
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
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
    ],
    keywords='pytest py.test types annotations pyannotate',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.5.0,!=3.5.1',
)
