import unittest
from unittest.mock import patch
from board import Board
from human_player import HumanPlayer


class TestHumanPlayer(unittest.TestCase):
    def setUp(self):
        self.board = Board(size=15, colors=False)
        self.human = HumanPlayer()

    @patch('builtins.input', side_effect=['9 9'])
    def test_legit_input_gives_y_and_x(self, input):
        assert self.human.get_move() == (9, 9)

    @patch('builtins.input', side_effect=['brfgs9 9'])
    def test_bogus_input_raises(self, input):
        with self.assertRaises(ValueError):
            self.human.get_move()
