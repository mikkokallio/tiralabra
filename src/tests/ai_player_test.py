import unittest
from board import Board
from AI_player import AIPlayer


class TestAIPlayer(unittest.TestCase):
    def setUp(self):
        self.board = Board(size=15)
        self.ai = AIPlayer(5, 2, 3, False, False, False, self.board)

    def test_ai_gives_a_move(self):
        self.board.add_piece(0, 0, 'X')
        y, x = self.ai.get_move(self.board, True, None)
        self.assertGreaterEqual(y, 0)
        self.assertLess(y, self.board.get_size())
        self.assertGreaterEqual(x, 0)
        self.assertLess(x, self.board.get_size())

    def test_ai_blocks_when_treatened(self):
        self.board.add_piece(5, 5, 'X')
        self.board.add_piece(4, 5, 'O')
        self.board.add_piece(5, 6, 'X')
        self.board.add_piece(4, 6, 'O')
        self.board.add_piece(5, 7, 'X')
        self.board.add_piece(5, 4, 'O')
        self.board.add_piece(5, 8, 'X')
        y, x = self.ai.get_move(self.board, True, None)
        self.assertEqual(y, 5)
        self.assertEqual(x, 9)

    def test_ai_finishes_row_despite_threat(self):
        self.board.add_piece(5, 5, 'O')
        self.board.add_piece(4, 5, 'X')
        self.board.add_piece(5, 6, 'O')
        self.board.add_piece(4, 6, 'X')
        self.board.add_piece(5, 7, 'O')
        self.board.add_piece(4, 7, 'X')
        self.board.add_piece(5, 8, 'O')
        self.board.add_piece(4, 8, 'X')
        y, x = self.ai.get_move(self.board, True, None)
        self.assertEqual(y, 5)
        self.assertIn(x, [4, 9])
