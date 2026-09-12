import unittest

from gdo.google_search.module_google_search import module_google_search


class GoogleSearchModuleTest(unittest.TestCase):
    def test_requires_network_support(self):
        self.assertEqual(['net'], module_google_search().gdo_dependencies())
