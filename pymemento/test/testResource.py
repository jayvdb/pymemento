import unittest
import pprint
import requests

import pymemento

pp = pprint.PrettyPrinter(indent=4)

class TestOriginalResource(unittest.TestCase):

    def test_getURIsFromHeaders(self):
      
        d = {'content-length': '190159', 'x-varnish': '705785075', 'x-content-type-options': 'nosniff', 'content-language': 'en', 'age': '0', 'vary': 'Accept-Encoding,Cookie', 'server': 'Apache', 'last-modified': 'Sat, 17 May 2014 16:48:28 GMT', 'connection': 'keep-alive', 'via': '1.1 varnish', 'link': '<http://ws-dl-05.cs.odu.edu/demo/index.php/Tyrion_Lannister>; rel="original latest-version",<http://ws-dl-05.cs.odu.edu/demo/index.php/Special:TimeGate/Tyrion_Lannister>; rel="timegate",<http://ws-dl-05.cs.odu.edu/demo/index.php/Special:TimeMap/Tyrion_Lannister>; rel="timemap"; type="application/link-format"', 'cache-control': 's-maxage=18000, must-revalidate, max-age=0', 'date': 'Sun, 29 Jun 2014 16:42:12 GMT', 'content-type': 'text/html; charset=UTF-8'}

        originalURI = 'http://ws-dl-05.cs.odu.edu/demo/index.php/Tyrion_Lannister'
        expectedURIG = 'http://ws-dl-05.cs.odu.edu/demo/index.php/Special:TimeGate/Tyrion_Lannister'
        expectedURIT = 'http://ws-dl-05.cs.odu.edu/demo/index.php/Special:TimeMap/Tyrion_Lannister'

        inputHeaders = requests.structures.CaseInsensitiveDict(d)

        orig = pymemento.OriginalResource(originalURI)

        actualURIG = orig._getURIFromRelation(inputHeaders, 'timegate')
        actualURIT = orig._getURIFromRelation(inputHeaders, 'timemap')

        self.assertEquals(expectedURIG, actualURIG, 'URI-G ' + str(actualURIG) + ' is incorrect')
        self.assertEquals(expectedURIT, actualURIT, 'URI-T ' + str(actualURIT) + ' is incorrect')

    def test_getURIsFromNoneInHeaders(self):
        
        inputHeaders = requests.structures.CaseInsensitiveDict()

        inputHeaders['content-length'] = '438'
        inputHeaders['accept-ranges'] = 'bytes'
        inputHeaders['server'] = 'Apache/2.2.15 (CentOS)'
        inputHeaders['last-modified'] = 'Sat, 09 Jun 2012 21:19:47 GMT'
        inputHeaders['connection'] = 'close'
        inputHeaders['etag'] = '"206ee-1b6-4c210ad2522c0"'
        inputHeaders['date'] = 'Sun, 29 Jun 2014 16:22:31 GMT'
        inputHeaders['content-type'] = 'text/html; charset=UTF-8'

        originalURI = 'http://www.littleprojects.net'

        orig = pymemento.OriginalResource(originalURI)

        self.assertIsNone(orig._getURIFromRelation(inputHeaders, 'timegate'))
        self.assertIsNone(orig._getURIFromRelation(inputHeaders, 'timemap'))
