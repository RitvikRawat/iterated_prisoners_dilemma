import sys
sys.path.append("../simulator")
import random
import unittest
from strategies.saint import Saint

class TestSaint(unittest.TestCase):
	def setUp(self):
		self.strat = Saint()

	def test_one_action(self):
		self.assertEqual(self.strat.get_next_move('anything'), 'cooperate', 'Did not return cooperate')

	def test_multiple_actions(self):
		ideal_responses = ['cooperate']*10
		opponent_actions = ['cooperate', 'defect']
		responses = [ self.strat.get_next_move(opponent_actions[random.randint(0,1)]) for _ in range(10)]
		self.assertEqual(responses, ideal_responses, 'Did not return cooperate for every move')

if __name__ == '__main__': 
	unittest.main()