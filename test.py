# STEP 1: Import required libraries
from random import random, uniform
import numpy as np

# STEP 2: Define the objective function f(x)
# f(x) = (x - 0.3)^3 - 5x + x^2 - 2
def f(x):
    return (x - 0.3)**3 - 5*x + x**2 - 2

# STEP 3: Define the SimulatedAnnealing class
class SimulatedAnnealing:
    def __init__(self, min_coordinate, max_coordinate, min_temp, max_temp, cooling_rate=0.02):
        self.min_coordinate = min_coordinate
        self.max_coordinate = max_coordinate
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.cooling_rate = cooling_rate
        self.actual_state = self.generate_random_x()
        self.best_state = self.actual_state

    # STEP 4: Implement the run method
    def run(self):
        temp = self.max_temp

        while temp > self.min_temp:
            next_state = self.generate_random_x()
            actual_energy = self.get_energy(self.actual_state)
            next_energy = self.get_energy(next_state)

            if next_energy > actual_energy:
                self.actual_state = next_state
            else:
                prob = self.accept_prob(actual_energy, next_energy, temp)
                if random() < prob:
                    self.actual_state = next_state

            if self.get_energy(self.actual_state) > self.get_energy(self.best_state):
                self.best_state = self.actual_state

            temp *= (1 - self.cooling_rate)

        print(f"Best solution found: x = {self.best_state}, f(x) = {self.get_energy(self.best_state)}")

    # STEP 5: Implement generate_random_x
    def generate_random_x(self):
        return uniform(self.min_coordinate, self.max_coordinate)

    # STEP 6: Implement accept_prob as a static method
    @staticmethod
    def accept_prob(actual_energy, next_energy, temp):
        if next_energy > actual_energy:
            return 1
        return np.exp((next_energy - actual_energy) / temp)

    # STEP 7: Implement get_energy as a static method
    @staticmethod
    def get_energy(x):
        return f(x)

# STEP 8: Run the algorithm in main block
if __name__ == '__main__':
    algorithm = SimulatedAnnealing(-2, 2, 1e-5, 100)
    algorithm.run()
