import sys
sys.path.append("../simulator")
import random
import unittest
from strategies.domstrat import Domstrat
class TestDomstrat(unittest.TestCase):
	def setUp(self):
		self.strat = Domstrat()

	def test_one_action(self):
		self.assertEqual(self.strat.get_next_move('anything'), 'defect', 'Did not return defect')

	def test_multiple_actions(self):
		ideal_responses = ['defect']*10
		responses = [None]*10
		for i in xrange(0,10):
			opponent_actions = ['first_move', 'cooperate', 'defect']
			rand_index = random.randint(0, 2)
			responses[i] = self.strat.get_next_move(opponent_actions[rand_index])
		self.assertEqual(responses, ideal_responses, 'Did not return defect for every move')

if __name__ == '__main__': 
	unittest.main()