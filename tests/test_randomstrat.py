import sys
sys.path.append("../simulator")
import random
import unittest
from strategies.randomstrat import Randomstrat

class TestRandomstrat(unittest.TestCase):
	def setUp(self):
		self.strat = Randomstrat()
		self.legal_moves = ['cooperate', 'defect']

	def test_one_action(self):
		legal_bool = self.strat.get_next_move('anything') in self.legal_moves
		self.assertEqual(legal_bool, True, 'Did not return legal move')

	def test_multiple_actions(self):
		response_list = [ self.strat.get_next_move('anything') for _ in range(10) ]
		legal_bool_list = [ response in self.legal_moves for response in response_list ]
		self.assertEqual(legal_bool_list, [True]*10, 'Did not return legal moves')

if __name__ == '__main__': 
	unittest.main()