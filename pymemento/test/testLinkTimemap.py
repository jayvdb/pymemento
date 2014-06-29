import unittest
import sys
import pprint

import pymemento

pp = pprint.PrettyPrinter(indent=4)

class TestLinkTimemap(unittest.TestCase):

    def test_from_file(self):

        timemap = """
    <http://a.example.org>;rel="original",
    <http://arxiv.example.net/timemap/http://a.example.org>
      ; rel="self";type="application/link-format"
      ; from="Tue, 20 Jun 2000 18:02:59 GMT"
      ; until="Wed, 09 Apr 2008 20:30:51 GMT",
    <http://arxiv.example.net/timegate/http://a.example.org>
      ; rel="timegate",
    <http://arxiv.example.net/web/20000620180259/http://a.example.org>
      ; rel="first memento";datetime="Tue, 20 Jun 2000 18:02:59 GMT"
      ; license="http://creativecommons.org/publicdomain/zero/1.0/",
    <http://arxiv.example.net/web/20091027204954/http://a.example.org>
       ; rel="last memento";datetime="Tue, 27 Oct 2009 20:49:54 GMT"
       ; license="http://creativecommons.org/publicdomain/zero/1.0/",
    <http://arxiv.example.net/web/20000621011731/http://a.example.org>
      ; rel="memento";datetime="Wed, 21 Jun 2000 01:17:31 GMT"
      ; license="http://creativecommons.org/publicdomain/zero/1.0/",
    <http://arxiv.example.net/web/20000621044156/http://a.example.org>
      ; rel="memento";datetime="Wed, 21 Jun 2000 04:41:56 GMT"
      ; license="http://creativecommons.org/publicdomain/zero/1.0/",
"""

        original = "http://a.example.org"
        expectedTimegate = "http://arxiv.example.net/timegate/http://a.example.org"
        expectedTimeMapURI = "http://arxiv.example.net/timemap/http://a.example.org"
        expectedFirstMementoURI = "http://arxiv.example.net/web/20000620180259/http://a.example.org"
        expectedSecondMementoURI = "http://arxiv.example.net/web/20000621011731/http://a.example.org"
        expectedThirdMementoURI = "http://arxiv.example.net/web/20000621044156/http://a.example.org"
        expectedLastMementoURI = "http://arxiv.example.net/web/20091027204954/http://a.example.org"
        expectedLicense = "http://creativecommons.org/publicdomain/zero/1.0/" 

        expectedMementos = [
            "http://arxiv.example.net/web/20000620180259/http://a.example.org",
            "http://arxiv.example.net/web/20000621011731/http://a.example.org",
            "http://arxiv.example.net/web/20000621044156/http://a.example.org",
            "http://arxiv.example.net/web/20091027204954/http://a.example.org",
        ]

        tm = pymemento.LinkTimemap.from_string(timemap, original)

        self.assertEquals(original, tm.original_uri,
            "original URI does not match")
        self.assertEquals(expectedTimegate, tm.timegate_uris[0],
            "timegate URI does not match")
        self.assertEquals(expectedTimeMapURI, tm.timemaps[0].uri_t,
            "timemap URI does not match")

        foundFirst = False
        foundSecond = False
        foundThird = False
        foundLast = False

        for key in tm.mementos.keys():
            for i in tm.mementos[key]:

                if 'first' in i.rels:
                    foundFirst = True
                    self.assertEquals(expectedFirstMementoURI, i.uri_m,
                        "first memento does not match")

                if 'last' in i.rels:
                    foundLast = True
                    self.assertEquals(expectedLastMementoURI, i.uri_m,
                        "last memento does not match")

                self.assertIn(
                    i.uri_m, expectedMementos,
                    "memento " + i.uri_m + " not in list of mementos")

                self.assertEquals(
                    expectedLicense, i.license_uri,
                    "unexpected license " + i.license_uri)

        self.assertTrue(foundFirst, "did not find first memento")
        self.assertTrue(foundLast, "did not find last memento")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLinkTimemap)
    unittest.TextTestRunner(verbosity=2).run(suite)
