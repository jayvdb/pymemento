# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import requests


class Resource(object):
    """
        Class for getting Memento information about a URI from
        the response headers returned from a request sent to the URI.
    """

    def __init__(self, URI):
        """
            Initialize the private member variables.

            Data other than the URI is lazy-loaded.
        """
        self._uri = URI
        self._headers = None
        self._request = None

    def getURIFromRelation(self, relation):
        """
            Get the URI from the Link header associated with the given
            relation.
        """
        self.performRequestIfNecessary()
        return self._getURIFromRelation(self._headers, relation)

    def performRequestIfNecessary(self):
        """
            This is the lazy loading for this class.  If we haven't 
            performed the request yet, do so to fill the private
            member variables.
        """
        if self._headers == None:
            self.repeatRequest()

    def repeatRequest(self):
        """
            Using the same URI, re-execute the request to fill the
            response headers list.
        """
        self._request = requests.head(url=self._uri)
        self._headers = self._request.headers

    def _getURIFromRelation(self, headers, relation):
        uri = None

        if 'link' in headers:
            for entry in requests.utils.parse_header_links(headers['link']):
                if 'rel' in entry:
                    if relation in entry['rel']:
                        uri = entry['url'] 
                        break

        return uri


class OriginalResource(Resource):
    """
        Class for getting Memento information about an original resource
        (URI-R).
    """
    def isTimeGate(self):
        """
            Determine if this URI-R is also operating as a TimeGate.
        """

        return self._uri == self.getURIFromRelation('timegate') 


class MementoResource(Resource):
    """
        Class for getting Memento information about a Memento resource
        (URI-M).
    """
    def getMementoDatetime(self):
        """
            Extract the Memento-Datetime from the response headers.
        """
        return self._headers['Memento-Datetime']
