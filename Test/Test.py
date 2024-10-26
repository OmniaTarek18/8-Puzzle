import unittest
from Algorithms.algorithm import *
from Algorithms.search_technique import *
from Heuristics.Euclidean import euclidean_heuristic
from Heuristics.Manhattan import manhattan_heuristic

class Test(unittest.TestCase):

    # check the number of inversions in the state
    def test_count_inversions(self):
        algo = Algorithm(123405678)
        inversions = algo.count_inversions(123405678)
        self.assertEqual(inversions, 0)
        inversions = algo.count_inversions(123456807)
        self.assertEqual(inversions, 1)
        inversions = algo.count_inversions(876543210)
        self.assertEqual(inversions, 7 + 6 + 5 + 4 + 3 + 2 + 1)
    # check if the initial state is solvable
    def test_isSolvable(self):
        initial_states = [
            312045678,
            125340678,
            125348670,
            125348607,
            125308647,
            125038647,
            125638047,
            125638407,
            125638470,
            125630478,
            123406758,
            123456708,
            867254301,
            867254031,
            876543210,
            87654321,
            806547231,
            125340678,
            142658730,
            102754863,
        ]
        for initial_state in initial_states:
            algo = Algorithm(initial_state)
            self.assertTrue(algo.is_solvable())
    # check if the initial state is not solvable
    def test_notSolvable(self):
        initial_states = [
            123456870,
            812043765,
            231054786,
            182453760
        ]
        for initial_state in initial_states:
            algo = Algorithm(initial_state)
            self.assertFalse(algo.is_solvable())
    # check if move is valid
    # get the location of the empty tile
    def test_get_empty_tile_location(self):
        algo = SearchTechnique.__new__(SearchTechnique, "A*", 123405678, 'Manhattan')
        self.assertEqual(algo.get_empty_tile_location(123405678), 4)
    # test if the move is valid
    def test_is_valid_move(self):
        algo = Algorithm(123456078)
        empty_tile = algo.get_empty_tile_location(algo.init_state)
        # Test move up
        self.assertTrue(algo.is_valid_move(empty_tile, -3))
        # Test move right
        self.assertTrue(algo.is_valid_move(empty_tile, 1))
        # Test move down
        self.assertFalse(algo.is_valid_move(empty_tile, 3))
        # Test move left
        self.assertFalse(algo.is_valid_move(empty_tile, -1))
    # check if the move is valid and apply the move if it is valid
    def test_apply_move(self):
        algo = Algorithm(123405678)
        empty_tile = algo.get_empty_tile_location(algo.init_state)
        # Test move up
        self.assertEqual(algo.apply_move(algo.init_state, empty_tile, -3), 103425678)
        # Test move right
        self.assertEqual(algo.apply_move(algo.init_state, empty_tile, 1), 123450678)
        # Test move down
        self.assertEqual(algo.apply_move(algo.init_state, empty_tile, 3), 123475608)
        # Test move left
        self.assertEqual(algo.apply_move(algo.init_state, empty_tile, -1), 123045678)
    # test Manhattan distance
    def test_manhattan_distance(self):
        heuristic = manhattan_heuristic(102345678, 12345678)
        self.assertEqual(heuristic, 1)
    # test Euclidean distance
    def test_euclidean_distance(self):
        heuristic = euclidean_heuristic(102345678, 12345678)
        self.assertEqual(heuristic, 1)

    def test_ids(self):
        ids = SearchTechnique("IDS", 867254301)
        ids.solve()
        self.assertEqual(ids.cost, 27)
        # self.assertEqual(ids.depth, 22)
        self.assertEqual(ids.nodes_explored, 27)





if __name__ == '__main__':
    unittest.main()
