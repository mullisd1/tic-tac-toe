import numpy as np
from unittest import TestCase

from tictactoe.board import Board


class Test_Win(TestCase):
	def test_row_win_O(self):
		board = Board(3)
		board.board = np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]])
		self.assertEqual(board.check_board(), 'O')

		board = Board(3)
		board.board = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
		self.assertEqual(board.check_board(), 'O')

		board = Board(3)
		board.board = np.array([[0, 0, 0], [0, 0, 0], [1, 1, 1]])
		self.assertEqual(board.check_board(), 'O')

	def test_row_win_X(self):
		board = Board(3)
		board.board = np.array([[-1, -1, -1], [0, 0, 0], [0, 0, 0]])
		self.assertEqual(board.check_board(), 'X')

		board = Board(3)
		board.board = np.array([[0, 0, 0], [-1, -1, -1], [0, 0, 0]])
		self.assertEqual(board.check_board(), 'X')

		board = Board(3)
		board.board = np.array([[0, 0, 0], [0, 0, 0], [-1, -1, -1]])
		self.assertEqual(board.check_board(), 'X')

	def test_col_win_O(self):
		board = Board(3)
		board.board = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
		self.assertEqual(board.check_board(), 'O')

		board = Board(3)
		board.board = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])
		self.assertEqual(board.check_board(), 'O')

		board = Board(3)
		board.board = np.array([[0, 0, 1], [0, 0, 1], [0, 0, 1]])
		self.assertEqual(board.check_board(), 'O')

	def test_col_win_X(self):
		board = Board(3)
		board.board = np.array([[-1, 0, 0], [-1, 0, 0], [-1, 0, 0]])
		self.assertEqual(board.check_board(), 'X')

		board = Board(3)
		board.board = np.array([[0, -1, 0], [0, -1, 0], [0, -1, 0]])
		self.assertEqual(board.check_board(), 'X')

		board = Board(3)
		board.board = np.array([[0, 0, -1], [0, 0, -1], [0, 0, -1]])
		self.assertEqual(board.check_board(), 'X')

	def test_diag_win_O(self):
		board = Board(3)
		board.board = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
		self.assertEqual(board.check_board(), 'O')

		board = Board(3)
		board.board = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
		self.assertEqual(board.check_board(), 'O')

	def test_diag_win_X(self):
		board = Board(3)
		board.board = np.array([[0, 0, -1], [0, -1, 0], [-1, 0, 0]])
		self.assertEqual(board.check_board(), 'X')

		board = Board(3)
		board.board = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])
		self.assertEqual(board.check_board(), 'X')
