'''A setuptools based setup module.

Authoritative references:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
'
'''

from setuptools import setup, find_packages

# Get the long description from the README file
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

import mynamespace.mypackage  # replace with the actual package name


setup(
    name='skeleton',
    version=mynamespace.mypackage.__version__,

    description='Python project skeleton',
    long_description=long_description,
    url='https://github.com/dtolpin/python-project-skeleton',

    packages=find_packages(exclude=['doc']),

    # source code layout
    namespace_packages=['mynamespace'],

    # Generating the command-line tool
    entry_points={
        'console_scripts': [
            'hello=mynamespace.mypackage.cmdline:hello',
	    'gdbye=mynamerspace.mypackage.cmdline:gdbye'
        ]
    },

    # author and license
    author='David Tolpin',
    author_email='david.tolpin@gmail.com',
    license='MIT',

    # dependencies, a list of rules
    install_requires=['overrides>=1.8'],
    # add links to repositories if modules are not on pypi 
    dependency_links=[
    ],

    #  PyTest integration
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
