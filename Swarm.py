import time

from Pallets import Pallets
from Particle import Particle
from Particle_With_LS import Particle_With_LS

class Swarm:
    """
    Represents a particle swarm for an instance of the pallet problem.
    """
    def __init__(self, pallet_problem : Pallets, cognitive_coefficient = 1.1193):        
        self.pallet_problem = pallet_problem
        Particle.COGNITIVE_COEFFICIENT = cognitive_coefficient
        Particle_With_LS.COGNITIVE_COEFFICIENT = cognitive_coefficient

    def timed_swarm_search(self, swarm_size: int, run_time: int):
        """
        Conduct a PSO swarm search for a solution to the pallet problem for a specified length of time.

        Parameters:
        swarm_size: number of particles in the swarm
        run_time: length of time (seconds) to search for

        Returns: a list containing the best solution found, followed by its cost
        """
        end_time = time.time() + run_time
        gbest = self.pallet_problem.generate_random_solution()
        gbest_cost = self.pallet_problem.evaluate_cost(gbest)
        self.particles = [None for x in range(swarm_size)]

        for i in range(swarm_size):
                self.particles[i] = Particle(self.pallet_problem, self.pallet_problem.generate_random_solution())

        while time.time() < end_time:
            for j in range(len(self.particles)):
                pbest = self.particles[j].update_particle(gbest)
                pbest_cost = self.pallet_problem.evaluate_cost(pbest)

                if pbest_cost < gbest_cost:
                    gbest = pbest
                    gbest_cost = pbest_cost

        #print(f"Best found by swarm search: {self.gbest} costing {self.gbest_cost}")
        return [gbest, gbest_cost]

    def timed_swarm_search_with_lsi(self, swarm_size: int, run_time: int):
        """
        Conduct a PSOwLSI swarm search for a solution to the pallet problem for a specified length of time.

        Parameters:
        swarm_size: number of particles in the swarm
        run_time: length of time (seconds) to search for

        Returns: a list containing the best solution found, followed by its cost
        """
        end_time = time.time() + run_time
        gbest = self.pallet_problem.generate_random_solution()
        gbest_cost = self.pallet_problem.evaluate_cost(gbest)
        self.particles = [None for x in range(swarm_size)]

        for i in range(swarm_size):
                self.particles[i] = Particle_With_LS(self.pallet_problem, self.pallet_problem.generate_random_solution())

        while time.time() < end_time:
            for j in range(len(self.particles)):
                pbest = self.particles[j].update_particle(gbest)
                pbest_cost = self.pallet_problem.evaluate_cost(pbest)

                if pbest_cost < gbest_cost:
                    gbest = pbest
                    gbest_cost = pbest_cost

        #print(f"Best found by swarm search: {self.gbest} costing {self.gbest_cost}")
        return [gbest, gbest_cost]