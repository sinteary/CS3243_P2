# CS3243 Project 2

## Task 1: Sudoku

**Approach 1:**
* Maintain assignable numbers for each empty cell on the board as constraints.
* Use backtracking to try all the assignable numbers for each cell in order.
	* If succeed, proceed to the next empty cell.
	* If failed, backtrack by resetting the current cell empty and go back to the previous assignment.
* After each valid assignment, update the constraints for all remaining empty cells on the board

**Results:**
* Input1: `24.9235s`
* Input2: `2.7022s`
* Input3: `2.1306s`
* Input4: `0.4958s`



## Task 2: The Pacman Game

### Basic Elements

`Direction` class: contains the the set of possible directions `{NORTH, SOUTH, EAST, WEST, STOP, LEFT, RIGHT, REVERSE}`

`Configuration` class: holds the (x, y) coordinates fo a character and its travelling direction

`AgentState` class: holds the state of an agent (config, speed, scared, ...)

`Actions` class: contains static methods for manipulating move actions

`Game` class: manages agents, rules, history, control flow etc


### Game State

The `GameState` class in `pacman.py` specifies the full game state, including the food, capsules, agent configurations and score changes.

It is used by the `Game` object to capture the actual state of the game and **also used by the agent to reason about the game**.

* `getLegalActions( self, agentIndex=0 )`: returns the legal actions for the specified agent

* `generateSuccessor( self, agentIndex, action)`: return the successor state after the specified agent takes an action



### Inheritance Tree
```
Agent                           (game.py)
|
 --> ValueEstimationAgent       (learningAgents.py) 
  |
   --> ReinforcementAgent       (learningAgents.py)
    |
     --> QlearningAgent         (qlearningAgents.py)
      |
       --> PacmanQAgent         (qlearningAgents.py)
        |
         --> ApproximateQAgent  (qlearningAgents.py)
```

```
FeatureExtractor              (featureExtractors.py)
|
 --> IdentityExtractor
|
 --> CoordinateExtractor
|
 --> SimpleExtractor (worth looking at implementation)
|
 --> NewExtractor (design your own)
```


**Agent**

* `getAction(self, state)`: receive a game state, return an action from Direction



**ValueEstimationAgent**

* Attributes:
```
alpha -------- learning rate
epsilon ------ exploration rate
gamma -------- discount factor
numTraining -- number of training episodes
```

* `getQValue(self, state, action)`: receive a game state & action, return Q(state, action)

* `getValue(self, state)`: return the value given a game state under the best action. 
i.e. `V(s) = max_{a in actions} Q(s,a)`

* `getPolicy(self, state)`: return the policy (best action to take given a state). 
i.e. `policy(s) = arg_max_{a in actions} Q(s,a)`

* `getAction(self, state)`: call `state.getLegalActions()`, choose an action and return it



**ReinforcementAgent**

* Attributes:
```
actionFn = lambda state: state.getLegalActions()
	(function that takes a state, returns a list of legal actions)
```

* `update(self, state, action, nextState, reward)`: get called after observing a transition & reward

* `getLegalActions(self,state)`: get available actions for a given state



**QLearningAgent**

* `getQValue(self, state, action)`: if a state has not seen, return 0.0; otherwise return Q(state, action)

* `computeValueFromQValues(self, state)`: return `max_action Q(state,action)` over legal actions; if no legal actions, return 0.0

* `computeActionFromQValues(self, state)`: compute the best action to take in a given state; if no legal action, return `None`

* `getAction(self, state)`: compute the action to take in the current state; if no legal action, return `None`

* `update(self, state, action, nextState, reward)`: called by parent class to observe `state = action => nextState & reward` transition; do the QValue update



**ApproximateQAgent**

* Attributes:
```
featExtractor = util.lookup(extractor, globals())()
weights = util.Counter()
```

* `getQValue(self, state, action)`: return `Q(state,action) = w * featureVector` where `*` is the dotProduct operator

* `update(self, state, action, nextState, reward)`: update weights based on transition



### Utility

**Functions**

* `manhattanDistance(xy1, xy2)`: return the Manhattan distance between points xy1 and xy2

* `flipCoin(p)`: return true with the given probability



**Counter**

A counter maintains counts for some keys. It extends from dictionary with number values (integer / float). 

```
{'test': 2, 'blah': 1, 'item': 5}
```

All keys are defaulted to have value 0. Hence, we can count things without initialisation.

```
a = Counter()
a['blah'] += 1
print(a['blah'])

The terminal will print 1 without error.
```

* `incrementAll(self, keys, count)`: increment all values of the keys by the same count

* `argMax(self)`: return the key with the highest value

* `sortedKeys(self)`: return a list of keys sorted by their values in descending order

* `totalCount(self)`: return the sum of counts for all keys

* `normalize(self)`: edit the counter such that total count of all keys equals 1. The ratio of counts for keys remains the same.

* `divideAll(self, divisor)`: divide all counts by divisor
