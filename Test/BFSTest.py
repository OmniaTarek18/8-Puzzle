import unittest
from Algorithms.search_technique import *


class BFSTest(unittest.TestCase):

    def test_BFS_1(self):
        bfs = SearchTechnique("BFS", 125340678)
        self.assertTrue(bfs.is_solvable())
        bfs.solve()
        self.assertEqual(bfs.cost, 3)
        self.assertEqual(bfs.nodes_explored, 5)
        self.assertEqual(bfs.depth, 3)


    def test_BFS_2(self):
        bfs = SearchTechnique("BFS", 142658730)
        self.assertTrue(bfs.is_solvable())
        bfs.solve()
        self.assertEqual(bfs.cost, 8)
        self.assertEqual(bfs.depth, 8)

    def test_BFS_3(self):
        bfs = SearchTechnique("BFS", 125630478)
        self.assertTrue(bfs.is_solvable())
        bfs.solve()
        self.assertEqual(bfs.cost, 11)
        self.assertEqual(bfs.depth, 11)






if __name__ == '__main__':
    unittest.main()
