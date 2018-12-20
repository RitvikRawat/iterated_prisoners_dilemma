import sys
sys.path.append("../simulator")

import unittest
from strategies.domstrat import Domstrat
class TestDomstrat(unittest.TestCase):
	def setUp(self):
		self.strat = Domstrat()

	def test_one_action(self):
		self.assertEqual(self.strat.get_next_move('anything'), 'defect', 'Did not return defect')

# if __name__ == '__main__': 
# 	unittest.main() 