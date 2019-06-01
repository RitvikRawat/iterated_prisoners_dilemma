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
for strat_1 in strategy_list:
	for strat_2 in strategy_list:
		print duel(strat_1, strat_2, no_of_runs)