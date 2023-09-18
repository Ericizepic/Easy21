import random 
from itertools import product

class MC_Agent(object):
    def __init__(self, alpha=1):
        self.states = list(product(range(1,22), range(1,11)))
        self.visit_count = {**{(item, 'hit'): 0 for item in self.states}, **{(item, 'stick'): 0 for item in self.states}}
        self.Q = {**{(item, 'hit'): 0 for item in self.states}, **{(item, 'stick'): 0 for item in self.states}}

        self.state_history = [] # state
        self.alpha = alpha

    # stochastic episodes are genearted off of an epsilon greedy algorithm. Decision to explore vs exploit is dependent
    # on the number of times the node itself has been explored
    def epsilon_greedy_action(self, s):
        epsilon = 100/(100 + self.visit_count[(s,'hit')] + self.visit_count[(s,'stick')])
        exploit = random.random() > epsilon
        if (self.Q[(s, 'hit')] > self.Q[(s, 'stick')] and exploit):
            return 'hit'
        elif (self.Q[(s, 'hit')] < self.Q[(s, 'stick')] and exploit):
            return 'stick'
        else:
            return 'hit' if random.random() > 0.5 else 'stick'

    # save the entire trajectory since Monte Carlo learning requires the end result
    def save_interval(self,s,a):
        self.state_history.append((s,a))
        self.visit_count[(s,a)] += 1

    # updated via montecarlo learning with step-value of 1/(# time state is visited)
    def learn(self, g_t):
        for (s,a) in self.state_history:
            self.Q[(s,a)] += (g_t - self.Q[(s,a)])/self.visit_count[(s,a)]

class SARSA_Agent(object):
    def __init__(self, alpha=1):
        self.states = list(product(range(1,22), range(1,11)))
        self.visit_count = {**{(item, 'hit'): 0 for item in self.states}, **{(item, 'stick'): 0 for item in self.states}}
        self.Q = {**{(item, 'hit'): 0 for item in self.states}, **{(item, 'stick'): 0 for item in self.states}}

        self.state_history = [] # state
        self.alpha = alpha

    # stochastic episodes are genearted off of an epsilon greedy algorithm. Decision to explore vs exploit is dependent
    # on the number of times the node itself has been explored
    def epsilon_greedy_action(self, s):
        epsilon = 100/(100 + self.visit_count[(s,'hit')] + self.visit_count[(s,'stick')])
        exploit = random.random() > epsilon
        if (self.Q[(s, 'hit')] > self.Q[(s, 'stick')] and exploit):
            return 'hit'
        elif (self.Q[(s, 'hit')] < self.Q[(s, 'stick')] and exploit):
            return 'stick'
        else:
            return 'hit' if random.random() > 0.5 else 'stick'

    # save the entire trajectory since Monte Carlo learning requires the end result
    def save_interval(self,s,a):
        self.state_history.append((s,a))
        self.visit_count[(s,a)] += 1

    # updated via montecarlo learning with step-value of 1/(# time state is visited)
    def learn(self, g_t):
        for (s,a) in self.state_history:
            self.Q[(s,a)] += (g_t - self.Q[(s,a)])/self.visit_count[(s,a)]