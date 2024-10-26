import unittest
from Algorithms.search_technique import *


class AStarTest(unittest.TestCase):
    # test A* algorithm with Manhattan heuristic
    def test_astar_manhattan(self):
        algo = SearchTechnique( "A*", 123456780, 'Manhattan', 12345678)
        algo.solve()
        self.assertEqual(algo.cost, 22)
        self.assertEqual(algo.depth, 22)
        algo.goal = 123456780
        algo.solve()
        self.assertEqual(algo.cost, 0)
        algo.goal = 123456708
        algo.solve()
        self.assertEqual(algo.cost, 1)
    # test A* algorithm with Euclidean heuristic
    def test_astar_euclidean(self):
        algo = SearchTechnique("A*", 123456780, 'Euclidean')
        algo.solve()
        self.assertEqual(algo.cost, 22)
        self.assertEqual(algo.depth, 22)
        algo.goal = 123456780
        algo.solve()
        self.assertEqual(algo.cost, 0)
        algo.goal = 123456708
        algo.solve()
        self.assertEqual(algo.cost, 1)
    # test A* algorithm with Manhattan and Euclidean heuristic
    def test_astar(self):
        manhattan = SearchTechnique("A*", 123456780, 'Manhattan')
        manhattan.solve()
        euclidean = SearchTechnique("A*", 123456780, 'Euclidean')
        euclidean.solve()
        self.assertEqual(manhattan.cost, 22)
        self.assertEqual(euclidean.cost, 22)
        self.assertTrue(euclidean.nodes_explored > manhattan.nodes_explored)
        self.assertTrue(manhattan.get_path() == euclidean.get_path())
    ###### 1
    # manhattan
    def test_Manhattan_1(self):
        manhattan = SearchTechnique("A*", 125340678,"Manhattan")
        self.assertTrue(manhattan.is_solvable())
        manhattan.solve()
        self.assertEqual(manhattan.cost, 3)
        self.assertEqual(manhattan.nodes_explored, 4)
        self.assertEqual(manhattan.depth, 3)
    # euclidean
    def test_Euclidean_1(self):
        euclidean = SearchTechnique("A*", 125340678,"Euclidean")
        self.assertTrue(euclidean.is_solvable())
        euclidean.solve()
        self.assertEqual(euclidean.cost, 3)
        self.assertEqual(euclidean.nodes_explored, 4)
        self.assertEqual(euclidean.depth, 3)
    # ###### 2
    # manhattan
    def test_Manhattan_2(self):
        manhattan = SearchTechnique("A*", 142658730,"Manhattan")
        self.assertTrue(manhattan.is_solvable())
        manhattan.solve()
        self.assertEqual(manhattan.cost, 8)
        self.assertEqual(manhattan.nodes_explored, 11)
        self.assertEqual(manhattan.depth, 8)
    # euclidean
    def test_Euclidean_2(self):
        euclidean = SearchTechnique("A*", 142658730,"Euclidean")
        self.assertTrue(euclidean.is_solvable())
        euclidean.solve()
        self.assertEqual(euclidean.cost, 8)
        self.assertEqual(euclidean.nodes_explored, 11)
        self.assertEqual(euclidean.depth, 8)
    ###### 3
    # manhattan
    def test_Manhattan_3(self):
        manhattan = SearchTechnique("A*", 102754863,"Manhattan")
        self.assertTrue(manhattan.is_solvable())
        manhattan.solve()
        self.assertEqual(manhattan.cost, 23)
        self.assertEqual(manhattan.depth, 23)
    # euclidean
    def test_Euclidean_3(self):
        euclidean = SearchTechnique("A*", 102754863,"Euclidean")
        self.assertTrue(euclidean.is_solvable())
        euclidean.solve()
        self.assertEqual(euclidean.cost, 23)
        self.assertEqual(euclidean.depth, 23)

if __name__ == '__main__':
    unittest.main()
