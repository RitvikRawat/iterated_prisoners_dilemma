import ConfigParser
import io
from strategies.domstrat import Domstrat
from strategies.saint import Saint
from strategies.tft import TFT
from strategies.randomstrat import Randomstrat
from run_duel import duel

# Load the configuration file
with open('../config.ini') as f:
	config_content = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(config_content))

no_of_runs = config.getint('simulation_run','no_of_runs')
# print duel(Domstrat(), TFT(), no_of_runs)

strategy_list = [Domstrat(), TFT(), Saint(), Randomstrat()]
score_table = [ ["null, null"]*len(strategy_list) for i in strategy_list ]
for i, strat_1 in enumerate(strategy_list):
	for j, strat_2 in enumerate(strategy_list):
		# print str(strat_1.strat_name)+','+str(strat_2.strat_name)
		score1, score2, _, _ = duel(strat_1, strat_2, no_of_runs)
		score_table[i][j] = str(score1)+'/'+str(score2)

label_score_table = [ [strategy_list[i].strat_name] + row for i, row in enumerate(score_table) ]
label_score_table = [ ["strategy names"] + [ strategy.strat_name for strategy in strategy_list] ] + label_score_table
print label_score_table

import csv
with open('../result/output.csv', 'w') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerows(label_score_table)