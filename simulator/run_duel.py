#!/usr/bin/env python

import ConfigParser
import io
from strategies.domstrat import Domstrat
from strategies.saint import Saint
from strategies.tft import TFT
from strategies.randomstrat import Randomstrat

# Load the configuration file
with open('../config.ini') as f:
	config_content = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(config_content))


def get_duel_payoff(action1, action2):
	return config.getint('game',action1+'_'+action2), config.getint('game',action2+'_'+action1)

def duel(strategy1, strategy2, no_of_runs):
	score1 = score2 = 0
	moves1 = [None]*no_of_runs
	moves2 = [None]*no_of_runs
	# subsequent moves. Opponents last move available
	old_action1 = old_action2 = 'first_move'
	for i in xrange(0,no_of_runs):
		action1 = strategy1.get_next_move(old_action2)
		action2 = strategy2.get_next_move(old_action1)
		payoff1, payoff2 =  get_duel_payoff(action1, action2)
		score1 += int(payoff1)
		score2 += int(payoff2)
		moves1[i] = action1
		moves2[i] = action2
		old_action1 = action1
		old_action2 = action2
	return score1, score2, moves1, moves2

no_of_runs = config.getint('simulation_run','no_of_runs')
print duel(Randomstrat(), TFT(), no_of_runs)