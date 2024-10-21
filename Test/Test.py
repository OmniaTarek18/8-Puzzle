import unittest

from stem.descriptor.export import export_csv

from Algorithms.search_technique import *
from Heuristics.Euclidean import euclidean_heuristic
from Heuristics.Manhattan import manhattan_heuristic
class Test(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_isSolvable(self):
       algo = SearchTechnique.__new__(SearchTechnique, "AStar", 123456780, 'Manhattan')
       self.assertTrue(algo.is_solvable())
       algo = SearchTechnique.__new__(SearchTechnique, "AStar", 210345678, 'Manhattan')
       self.assertFalse(algo.is_solvable())


    def test_apply_move(self):
        algo = SearchTechnique.__new__(SearchTechnique, "AStar", 123405678,'Manhattan')
        empty_tile = algo.get_empty_tile_location(algo.init_state)
        # Test move up
        self.assertEqual(algo.apply_move(algo.init_state, empty_tile, -3), 103425678)
        # Test move right
        self.assertEqual(algo.apply_move(algo.init_state, empty_tile, 1), 123450678)
        # Test move down
        self.assertEqual(algo.apply_move(algo.init_state, empty_tile, 3), 123475608)
        # Test move left
        self.assertEqual(algo.apply_move(algo.init_state, empty_tile, -1), 123045678)

    def test_get_empty_tile_location(self):
        algo = SearchTechnique.__new__(SearchTechnique, "AStar", 123405678,'Manhattan')
        self.assertEqual(algo.get_empty_tile_location(123405678), 4)

    def test_manhattan_distance(self):
        heuristic = manhattan_heuristic(102345678, 12345678)
        self.assertEqual(heuristic, 2)

    def test_euclidean_distance(self):
        heuristic = euclidean_heuristic(102345678, 12345678)
        self.assertEqual(heuristic, 2)

    def test_astar_manhattan(self):
        algo = SearchTechnique.__new__(SearchTechnique, "AStar", 123456780,'Manhattan',12345678)
        solution = algo.solve()
        self.assertEqual(algo.cost, 22)
        self.assertEqual(algo.depth, 22)
        algo.goal = 123456780
        solution = algo.solve()
        self.assertEqual(algo.cost, 0)
        algo.goal = 123456708
        solution = algo.solve()
        self.assertEqual(algo.cost, 1)


    def test_astar_euclidean(self):
        algo = SearchTechnique.__new__(SearchTechnique, "AStar", 123456780,'Euclidean')
        solution = algo.solve()
        self.assertEqual(algo.cost, 22)
        self.assertEqual(algo.depth, 22)


    def test_astar(self):
        manhattan = SearchTechnique.__new__(SearchTechnique, "AStar", 123456780,'Manhattan')
        manhattan.solve()
        euclidean = SearchTechnique.__new__(SearchTechnique, "AStar", 123456780,'Euclidean')
        euclidean.solve()
        self.assertEqual(manhattan.cost, 22)
        self.assertEqual(euclidean.cost, 22)
        self.assertTrue(euclidean.nodes_explored>manhattan.nodes_explored)
        self.assertTrue(manhattan.get_path() == euclidean.get_path())





if __name__ == '__main__':
    unittest.main()
