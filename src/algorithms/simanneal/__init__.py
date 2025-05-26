import math
import random
import time

class SimulatedAnnealingTSP:
    def __init__(self, cities, initial_temp=10000, cooling_rate=0.995, stopping_temp=1e-8, max_iter=1000):
        self.cities = cities
        self.N = len(cities)
        self.temp = initial_temp
        self.cooling_rate = cooling_rate
        self.stopping_temp = stopping_temp
        self.max_iter = max_iter

    def distance(self, city1, city2):
        return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

    def total_distance(self, path):
        return sum(self.distance(path[i], path[(i + 1) % self.N]) for i in range(self.N))

    def swap_two(self, path):
        new_path = path[:]
        i, j = random.sample(range(self.N), 2)
        new_path[i], new_path[j] = new_path[j], new_path[i]
        return new_path

    def accept_probability(self, old_cost, new_cost, temp):
        if new_cost < old_cost:
            return 1.0
        return math.exp(-(new_cost - old_cost) / temp)

    def run(self):
        current_path = self.cities[:]
        random.shuffle(current_path)
        current_cost = self.total_distance(current_path)
        best_path = current_path[:]
        best_cost = current_cost

        start_time = time.time()
        iteration = 0

        while self.temp > self.stopping_temp and iteration < self.max_iter:
            new_path = self.swap_two(current_path)
            new_cost = self.total_distance(new_path)

            if self.accept_probability(current_cost, new_cost, self.temp) > random.random():
                current_path = new_path
                current_cost = new_cost
                if new_cost < best_cost:
                    best_path = new_path
                    best_cost = new_cost

            self.temp *= self.cooling_rate
            iteration += 1

        return best_path, best_cost, time.time() - start_time
