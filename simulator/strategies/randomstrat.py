import random

class Randomstrat:
	def __init__(self):
		self.strat_name = 'Random strategy'
	def get_next_move(self, opponent_move):
		if random.randint(0, 1) == 0:
			return 'cooperate'
		else:
			return 'defect'