# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import requests


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
        self._headers = None

    def getURIFromRelation(self, relation):
        """
            Get the URI from the Link header associated with the given
            relation.
        """
      
        performRequestIfNecessary()

        return self._getURIFromRelation(self._headers, relation)

    def performRequestIfNecessary():
        """
            This is the lazy loading for this class.  If we haven't 
            performed the request yet, do so to fill the private
            member variables.
        """
        if self._headers == None:
            repeatRequest()

    def repeatRequest():
        """
            Using the same URI-R, re-execute the request to fill the
            response headers list.
        """
        r = requests.head(url=self._urir)
        self._headers = r.headers

    def _getURIFromRelation(self, headers, relation):
        uri = None

        if 'link' in headers:
            for entry in requests.utils.parse_header_links(headers['link']):
                if relation in entry['rel']:
                    uri = entry['url'] 
                    break

        return uri
