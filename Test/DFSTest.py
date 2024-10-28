import unittest
from Algorithms.search_technique import *

class DFSTest(unittest.TestCase):

    def test_DFS_1(self):
        dfs = SearchTechnique("DFS", 312645078)
        self.assertTrue(dfs.is_solvable())
        dfs.solve()
        self.assertEqual(dfs.cost, 2)
        self.assertEqual(dfs.nodes_explored, 3)
        self.assertEqual(dfs.depth, 2)

    def test_DFS_2(self):
        dfs = SearchTechnique("DFS", 125340678)
        self.assertTrue(dfs.is_solvable())
        dfs.solve()
        self.assertEqual(dfs.cost, 3)
        self.assertEqual(dfs.nodes_explored, 4)
        self.assertEqual(dfs.depth, 3)

    def test_DFS_3(self):
        dfs = SearchTechnique("DFS", 120345678)
        self.assertTrue(dfs.is_solvable())
        dfs.solve()
        self.assertTrue(dfs.cost>2)

    def test_DFS_4(self):
        dfs = SearchTechnique("DFS", 123456780)
        self.assertTrue(dfs.is_solvable())
        dfs.solve()
        self.assertTrue(dfs.cost>100)









if __name__ == '__main__':
    unittest.main()
