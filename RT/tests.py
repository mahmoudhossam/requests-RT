#!/usr/bin/python
from rt import RT
import unittest, os

class TestRT(unittest.TestCase):

    def testSearch(self):
        #get the api key from the environment
        api = RT(os.getenv('API_KEY'))
        result = api.search('inception')
        self.assertEqual(result.name, 'Inception')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRT)
    unittest.TextTestRunner(verbosity=2).run(suite)