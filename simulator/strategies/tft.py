class TFT:
	def __init__(self):
		self.strat_name = 'Tit for Tat'
	def get_next_move(self, opponent_move):
		if opponent_move == 'first_move':
			return 'cooperate'
		else:
			return opponent_move