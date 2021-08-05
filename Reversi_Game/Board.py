from Player import Player

class Board():
	def __init__(self, scale=8):
		self.scale = scale
		self.board = [[' '] * 8 for _ in range(self.scale)]

	def draw_board(self):
		x = '  '+'+---' * self.scale + '+'
		y = '  '+'|   ' * self.scale + '|'

		print('  '+'1    2    3    4    5    6    7    8')
		print(x)
		for i in range(8):
			print(y)
			print(i+1, end=' ')
			for m in range(8):
				print('| %s' % (self.board[m][i]), end=' ')
			print('|')
			print(y)
			print(x)

	def duplicate_board(self):
		dupBoard = Board()

		for x in range(self.scale):
			for y in range(self.scale):
				dupBoard[x][y] = self.board[x][y]

		return dupBoard



	def reset(self):
		"""
		default location is (3, 3), (3, 4), (4, 3), (4, 4) when scale = 8
		scale should be even number
		:return: a new board
		"""
		for x in range(self.scale):
			for y in range(self.scale):
				self.board[x][y] = ' '

		# Starting pieces:
		# self.board[3][3] = 'X'
		# self.board[3][4] = 'O'
		# self.board[4][3] = 'O'
		# self.board[4][4] = 'X'

		self.board[self.scale//2][self.scale//2] = 'X'
		self.board[self.scale//2][self.scale//2 + 1] = 'O'
		self.board[self.scale//2 + 1][self.scale//2] = 'O'
		self.board[self.scale//2 + 1][self.scale//2 + 1] = 'X'

	def is_Corner(x, y):
		return (x == 0 and y == 0) or (x == 7 and y == 0) or \
			   (x == 0 and y == 7) or (x == 7 and y == 7)

	def is_in_board(self, x, y):
		return (x >= 0 and x <= self.scale and y >= 0 and y <= self.scale)

	def is_valid_move(self, tile, xPlayed, yPlayed):
		if self.board[xPlayed][yPlayed] != ' ' or not self.is_in_board(x,y):
			return False
		self.board[xPlayed][yPlayed] = tile

		if tile == 'X':
			oppTile = 'O'
		else:
			oppTile = 'X'

		flipLocation = []
		for xDirection, yDirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
			x, y = xPlayed, yPlayed

			x += xDirection
			y += yDirection

			if self.is_in_board(x, y) and self.board[x][y] == oppTile:
				x += xDirection
				y += yDirection
				if not self.is_in_board(x,y):
					continue
				while self.board[x][y] == oppTile:
					x += xDirection
					y += yDirection
					if not self.is_in_board(x, y):
						break

				if not self.is_in_board(x, y):
					continue
				if self.board[x][y] == tile:
					while True:
						x -= xDirection
						y -= yDirection

						if x == xPlayed and y == yPlayed:
							break
						flipLocation.append([x, y])

		self.board[xPlayed][yPlayed] = ' '

		if len(flipLocation) == 0:
			return False
		return flipLocation

	def get_valid_move(self, player):
		valid_moves =[]

		for x in range(self.scale):
			for y in range(self.scale):
				if self.is_valid_move(self.board, player, x, y):
					valid_moves.append([x, y])

		return valid_moves

	def moveHint(self, player):
