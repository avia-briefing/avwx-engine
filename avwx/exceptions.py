"""
Contains avwx custom exceptions
"""


class InvalidRequest(Exception):
    """
    Unable to fetch data
    """


class SourceError(Exception):
    """
    Source servers returned an error code
    """
