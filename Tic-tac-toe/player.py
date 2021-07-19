import math
import random


class Player:
	def __init__(self, symbol):
		# symbol x or o
		self.symbol = symbol

	def get_move(self, game):
		pass

class HumanPlayer(Player):
	def __init__(self, symbol):
		super().__init__(symbol)
		
	def get_move(self, game):
		valid_square = False
		val = None
		while not valid_square:
			square = input(self.symbol + " \'s turn. Input move (0-9): " )
			try:
				val = int(square)
				if val not in game.available_moves():
					raise ValueError
				valid_square = True
			except ValueError:
				print("Invalid square")

		return val
