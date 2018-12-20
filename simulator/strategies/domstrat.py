class Domstrat:
	def __init__(self):
		self.strat_name = 'Dominant strategy (always defect)'
	def get_next_move(self, opponent_move):
		return 'defect'