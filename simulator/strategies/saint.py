class Saint:
	def __init__(self):
		self.strat_name = 'Saintly strategy (always cooperate)'
	def get_next_move(self, opponent_move):
		return 'cooperate'