import numpy as np


class Board:
	def __init__(self, size: int = 3):
		"""
		:info: init tic-tac-toe of (size)
		:param size: size of board
		"""
		self.size = size
		self.board = np.zeros((size, size))
		self.turn = 'X'

	def get_turn(self) -> str:
		"""
		:info: get turn
		:return: turn
		"""
		return self.turn

	def set_turn(self):
		"""
		:info: set correct turn when board is set
		:return: none
		"""
		if self.board.sum() < 0:
			self.turn = 'O'
		else:
			self.turn = 'X'
		return self.turn

	def validate_pos(self, row: int, col: int) -> bool:
		"""
		:info: validates row and column inputs
		:param row: row input
		:param col: col input
		"""
		if row < 0 or row >= self.size:
			raise ValueError(f'Row {row}: is out of bounds on board of {self.size}')

		if col < 0 or col >= self.size:
			raise ValueError(f'Row {row}: is out of bounds on board of {self.size}')

		if self.board[row][col] != 0:
			raise ValueError(f'Board Position [{row}, {col}] is not empty')
		return True

	def flip_turn(self):
		"""
		:info: flips the value of turn between [O, X]
		"""
		if self.turn == 'X':
			self.turn = 'O'
		else:
			self.turn = 'X'

	def place_val(self, row: int, col: int, val: int):
		"""
		:info: places value
		:param row: row input
		:param col: col input
		:param val: value to put on board
		"""
		if self.validate_pos(row, col):
			self.board[row][col] = val
			self.flip_turn()
			return True
		return False

	def place(self, row: int, col: int) -> bool:
		"""
		:info: place y
		:param row: row input
		:param col: col input
		"""
		if self.turn == 'X':
			self.place_x(row, col)
			return True
		elif self.turn == 'O':
			self.place_o(row, col)
			return True
		return False

	def place_x(self, row: int, col: int) -> bool:
		"""
		:info: place x
		:param row: row input
		:param col: col input
		"""
		return self.place_val(row, col, -1)

	def place_o(self, row: int, col: int) -> bool:
		"""
		:info: place y
		:param row: row input
		:param col: col input
		"""
		return self.place_val(row, col, 1)

	def check_board(
		self,
	):
		"""
		:info: checks if the game has been won
		:param:
		:return:
		"""
		sums = []

		## Diagnals
		sums.extend(list(np.sum(self.board, axis=0)))
		sums.extend(list(np.sum(self.board, axis=1)))
		sums.append(self.board.diagonal().sum())
		sums.append(np.flipud(self.board).diagonal().sum())

		for _sum in sums:
			if abs(_sum) == self.size:
				if _sum < 0:
					return 'X'
				else:
					return 'O'

		full_rows = 0
		for row in self.board:
			if 0 not in row:
				full_rows += 1
		if full_rows == self.size:
			return 'Draw'
		return '-'

	def num_to_str(self, num: int) -> str:
		"""
		:info: converts number to output string
		:param num: num == -1,0,1

		"""
		valid_inputs = [-1, 0, 1]
		if num not in valid_inputs:
			raise ValueError(f'{num} is not in {valid_inputs}')

		if num == -1:
			return 'X'
		elif num == 1:
			return 'O'
		return ' '

	def str_to_num(self, p: str) -> str:
		"""
		:info: converts string to num
		:param p: str == X, O

		"""
		if p == 'X':
			return -1
		return 1

	def print_board(
		self,
	):
		num_cols = self.size + 1
		num_rows = self.size + 1

		out = ''
		for i in range(num_rows):
			### Top Line
			out += '+' + '---+' * (num_cols) + '\n'

			### Vals
			out += '|'
			if i == 0:
				out += '   |' + ''.join([f' {j} |' for j in range(self.size)])
			else:
				out += f' {i - 1} |'
				for j in self.board[i - 1][:]:
					out += f' {self.num_to_str(j)} |'
			out += '\n'

		### Bottom Line
		out += '+' + '---+' * (num_cols) + '\n'

		print(out)

	def set_board(self, board):
		self.size = board.shape[0]
		self.board = board
		self.set_turn()

	def to_str(self):
		return np.array2string(self.board.flatten())

	def minimax(self, depth, is_maximizing):
		cur_out = self.check_board()
		if cur_out == self.turn:
			return 1
		elif cur_out == 'Draw':
			return 0
		elif cur_out == '-':
			pass
		else:
			return -1

		if is_maximizing:
			best_score = -np.inf
			for i in range(self.size):
				for j in range(self.size):
					if self.board[i][j] == 0:
						self.board[i][j] = self.player
						score = self.minimax(depth + 1, False)
						self.board[i][j] = 0
						best_score = max(best_score, score)
			return best_score
		else:
			best_score = np.inf
			for i in range(self.size):
				for j in range(self.size):
					if self.board[i][j] == 0:
						self.board[i][j] = -1 * self.player
						score = self.minimax(depth + 1, True)
						self.board[i][j] = 0
						best_score = min(best_score, score)
			return best_score

	def get_moves(self):
		best_score = -np.inf
		moves = []

		self.player = self.str_to_num(self.turn)

		for i in range(self.size):
			for j in range(self.size):
				if self.board[i][j] == 0:
					self.board[i][j] = self.player
					score = self.minimax(0, False)
					self.board[i][j] = 0
					if score > best_score:
						best_score = score
						moves = [(i, j)]
					elif score == best_score:
						moves.append((i, j))
		return moves

	def get_best_moves(self, board):
		self.size = board.shape[0]
		self.board = board
		self.set_turn()

		return self.get_moves()
