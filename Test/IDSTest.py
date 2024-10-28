import unittest
from Algorithms.search_technique import *


class IDSTest(unittest.TestCase):
    def test_IDS_1(self):
        ids = SearchTechnique("IDS", 125340678)
        ids.solve()
        ids.get_path()
        self.assertTrue(ids.is_solvable())
        self.assertEqual(ids.cost, 3)
        self.assertEqual(ids.depth, 3)

    def test_IDS_2(self):
        ids = SearchTechnique("IDS", 142658730)
        ids.solve()
        ids.get_path()
        self.assertTrue(ids.is_solvable())
        self.assertEqual(ids.cost, 8)
        self.assertEqual(ids.depth, 8)

    def test_IDS_3(self):
        ids = SearchTechnique("IDS", 125630478)
        ids.solve()
        ids.get_path()
        self.assertTrue(ids.is_solvable())
        self.assertEqual(ids.cost, 11)
        self.assertEqual(ids.depth, 11)

    def test_IDS_4(self):
        ids = SearchTechnique("IDS", 102754863)
        ids.solve()
        ids.get_path()
        self.assertTrue(ids.is_solvable())
        self.assertEqual(ids.cost, 23)
        self.assertEqual(ids.depth, 23)



if __name__ == '__main__':
    unittest.main()
