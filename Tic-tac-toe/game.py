class TicTacToe:
	def __init__(self):
		#This is 3x3 board
		self.board = [" " for _ in range(9)]
		self.current_winner = False #winner tracker

	def show_board(self):
		#This setting the row and columns

		"""
		rows = []
		for i in range (3):
			rows = self.board[i*3:(i+1)*3]

		for row in rows:
			print("|" + "|". join(row) + "|")
		:return:
		"""
		for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
			print("| " + " | ". join(row) + " |")

	@staticmethod
	def board_detail(self):
		"""
		This show board location such as
		|1|2|3|
		|4|5|6|
		|7|8|9|
		:return:
		"""
		detail_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
		for row in detail_board:
			print("| " + " | ".join(row) + " |")

	def avaliable_move(self):
		"""
		move = []
		for (i,spot) in enumerate(self.board):
			# ["x", "x", "o"] -> [(0,"x"), (1,"x"), (2, "o")]
			if spot == " ":
				move.append(i)
		return move
		:return:
		"""

		return [i for i, spot in enumerate(self.board) if spot == " "]

