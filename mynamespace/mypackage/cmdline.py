"""Command line entry points.
"""

import argparse
from . import __version__


def hello():
    """ Hello world sample entry point.
    """
    printf("hello world version {}".format(__version__))


def gdbye():
    """ Goodbye sample entry point.
    """
    printf("Goodbye version {}".format(__version__))
