#!/usr/bin/python
from rt import RT
import unittest, os

class TestRT(unittest.TestCase):

    def setUp(self):
        #get the api key from the environment
        self.api = RT(os.getenv('API_KEY'))

    def testSearch(self):
        self.result = self.api.search('Inception')
        self.assertEqual(self.result.name, 'Inception')

    def testRatings(self):
        self.result = self.api.search('Inception')
        self.assertEqual(self.result.critics_score, 86)

    def testMultipleResults(self):
        self.result = self.api.search('Austin Powers')
        self.assertTrue(isinstance(self.result, list))
    
    def testCast(self):
        self.result = self.api.cast('770672122')
        tom_hanks = self.result[0]
        self.assertEqual(tom_hanks.name, 'Tom Hanks')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRT)
    unittest.TextTestRunner(verbosity=2).run(suite)