import random 
from itertools import product

class MCAgent(object):
    def __init__(self, alpha=1):
        self.states = list(product(range(1,22), range(1,11)))
        self.visit_count = {**{(item, 'hit'): 0 for item in self.states}, **{(item, 'stick'): 0 for item in self.states}}
        self.Q = {**{(item, 'hit'): 0 for item in self.states}, **{(item, 'stick'): 0 for item in self.states}}

        self.state_history = [] # state
        self.alpha = alpha

    def epsilon_greedy_action(self, s, k):
        epsilon = 100/(100 + self.visit_count[(s,'hit')] + self.visit_count[(s,'stick')])
        exploit = random.random() > 1/k
        if (self.Q[(s, 'hit')] > self.Q[(s, 'stick')] and exploit):
            return 'hit'
        elif (self.Q[(s, 'hit')] < self.Q[(s, 'stick')] and exploit):
            return 'stick'
        else:
            return 'hit' if random.random() > 0.5 else 'stick'

    def save_interval(self,s,a):
        self.state_history.append((s,a))
        self.visit_count[(s,a)] += 1

    def learn(self, g_t):
        for (s,a) in self.state_history:
            self.Q[(s,a)] += (g_t - self.Q[(s,a)])/self.visit_count[(s,a)]