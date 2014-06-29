# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import requests


# TODO: lazy loading, reload function if they want to request again
class OriginalResource(object):
    """
        Class for getting information about a URI-R (original resource) from
        the response headers returned from a request sent to the URI-R.
        originaURI - the URI-R
    """

    def __init__(self, originalURI):
        """
            Initialize the private member variables.

            Other data is lazy-loaded.
        """
        self._urir = originalURI

    def _getURIGFromHeaders(self, headers):
      
        urig = None

        if 'link' in headers:
            raise NotImplementedError("not ready to scan link header yet")

        return urig

    def _getURITFromHeaders(self, headers):
      
        urit = None

        if 'link' in headers:
            raise NotImplementedError("not ready to scan link header yet")

        return urit
