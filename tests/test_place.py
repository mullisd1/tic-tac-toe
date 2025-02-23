from unittest import TestCase

from tictactoe.board import Board


class Test_Place(TestCase):
	def test_place(self):
		board = Board(3)
		board.board = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
		try:
			board.place(0, 0)
		except ValueError:
			pass
		else:
			raise AssertionError('ValueError was not raised')

	def test_place_neg(self):
		board = Board(3)
		board.board = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
		try:
			board.place(-1, -1)
		except ValueError:
			pass
		else:
			raise AssertionError('ValueError was not raised')

	def test_place_over(self):
		board = Board(3)
		board.board = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
		try:
			board.place(4, 4)
		except ValueError:
			pass
		else:
			raise AssertionError('ValueError was not raised')
