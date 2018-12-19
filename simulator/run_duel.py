#!/usr/bin/env python

import ConfigParser
import io
from strategies.domstrat import Domstrat

# Load the configuration file
with open('../config.ini') as f:
	config_content = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(config_content))


def get_payoff(action1, action2):
	return config.getint('game',action1+'_'+action2), config.getint('game',action2+'_'+action1)
def duel(strategy1, strategy2, no_of_runs):
	action1 = strategy1.get_next_move('first_move')
	action2 = strategy2.get_next_move('first_move')
	print get_payoff(action1, action2)
	for i in xrange(1,no_of_runs):
		action1 = strategy1.get_next_move('first_move')
		action2 = strategy2.get_next_move('first_move')
		print get_payoff(action1, action2)
no_of_runs = config.getint('simulation_run','no_of_runs')
duel(Domstrat(no_of_runs), Domstrat(no_of_runs), no_of_runs)