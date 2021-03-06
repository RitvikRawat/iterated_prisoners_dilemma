# Iterated Prisoner's Dilemma
Simulation of [Iterated Prisoner's Dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma#The_iterated_prisoner's_dilemma) strategies based on the work by [Robert Axelrod](http://www-personal.umich.edu/~axe/) in *The Evolution of Cooperation* (New York: Basic Books, 1984) 

Currently supports 4 strategies:
1. **domstrat**: Using the dominant strategy in the Prisoner's Dilemma game, this strategy always plays "defect".
2. **randomstrat**: This strategy randomly plays "defect" or "cooperate".
3. **saint**: This strategy always plays "cooperate".
4. **tft**: This is the tit for tat strategy. It starts with "cooperate" and then copies the move of the opponent.

## To run the simulation
```
cd simulator
python run_match.py
```
Results of the run can be found in result/output.csv

The (i,j)th cell represents Strategy 1 score/Strategy 2 score
