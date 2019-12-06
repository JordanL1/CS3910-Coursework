import Pallets
import random

class Particle:
    INERTIAL_COEFFICIENT = 0.721
    COGNITIVE_COEFFICIENT = 1.1193
    SOCIAL_COEFFICIENT = 1.1193

    def __init__(self, pallet_problem : Pallets, initial_solution):
        self.pallet_problem = pallet_problem
        self.position = initial_solution
        self.pbest = self.position
        self.pbest_cost = self.pallet_problem.evaluate_cost(self.pbest)

        self.velocity = []
        random_position = self.pallet_problem.generate_random_solution()

        # Set initial velocity to half the difference between a random position and the initial position
        for i in range(len(random_position)):
            velocity[i] = (random_position[i] - self.position[i]) / 2

    def calculate_new_velocity(self, gbest):
        new_velocity = []
        
        for i in range(len(self.velocity)):
            new_velocity[i] = (self.INERTIAL_COEFFICIENT * self.velocity[i]) 
            + self.COGNITIVE_COEFFICIENT * random.random() * (self.pbest[i] - self.position[i])
            + self.SOCIAL_COEFFICIENT * random.random() * (gbest[i] - self.position[i])
        
        return new_velocity