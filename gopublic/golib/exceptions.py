from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from future import standard_library

standard_library.install_aliases()


class GopublishParameterError(Exception):
    """Raised when the API returns an error"""
    pass


class GopublishApiError(Exception):
    """Raised when the API returns an error"""
    pass


class GopublishConnectionError(Exception):
    """Raised when the connection to the Gopublish server fails"""
    pass


class GopublishNotImplementedError(Exception):
    """Raised when there are not endpoint associated with this function"""
    pass


class GopublishTokenMissingError(Exception):
    """Raised when the gopublish token is missing"""
    pass
