import sys
sys.path.append("../simulator")
import random
import unittest
from strategies.tft import TFT

class TestTFT(unittest.TestCase):
	def setUp(self):
		self.strat = TFT()

	def test_opening_action(self):
		self.assertEqual(self.strat.get_next_move('first_move'), 'cooperate', 'Did not return cooperate')
	
	def test_multiple_actions(self):
		opponent_actions = ['cooperate', 'defect']
		opponent_moves_observed = [ opponent_actions[random.randint(0, 1)] for _ in range(9) ]
		responses = ['cooperate'] + [ self.strat.get_next_move(move) for move in opponent_moves_observed]
		self.assertEqual(responses, ['cooperate'] + opponent_moves_observed, 'Did not copy opponent moves')

if __name__ == '__main__': 
	unittest.main()