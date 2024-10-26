import unittest
from Algorithms.search_technique import *


class IDSTest(unittest.TestCase):
    def test_IDS_1(self):
        ids = SearchTechnique("IDS", 123405678)
        ids.solve()
        ids.get_path()
        self.assertTrue(ids.is_solvable())
        self.assertEqual(ids.cost, 4)
        self.assertEqual(ids.nodes_explored, 0)
        self.assertEqual(ids.depth, 4)



if __name__ == '__main__':
    unittest.main()
