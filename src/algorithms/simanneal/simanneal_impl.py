import time
import math
import random
from simanneal import Annealer

class TSPAnnealer(Annealer):
    def __init__(self, state):
        super().__init__(state)
        self.N = len(state)

    def move(self):
        i, j = sorted(random.sample(range(self.N), 2))
        self.state[i:j+1] = reversed(self.state[i:j+1])

    def energy(self):
        return sum(
            math.sqrt((self.state[i][0] - self.state[(i+1)%self.N][0])**2 +
                      (self.state[i][1] - self.state[(i+1)%self.N][1])**2)
            for i in range(self.N)
        )

def run_simanneal(cities, steps=1000):
    tsp = TSPAnnealer(cities[:])
    tsp.steps = steps
    start = time.time()
    best_state, cost = tsp.anneal()
    duration = time.time() - start
    return best_state, cost, duration
