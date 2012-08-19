#!/usr/bin/python
from rt import RT
import unittest, os

class TestRT(unittest.TestCase):

    def setUp(self):
        #get the api key from the environment
        self.api = RT(os.getenv('API_KEY'))
        self.result = self.api.search('Inception')

    def testSearch(self):
        self.assertEqual(self.result.name, 'Inception')

    def testRatings(self):
        self.assertEqual(self.result.critics_score, 86)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRT)
    unittest.TextTestRunner(verbosity=2).run(suite)