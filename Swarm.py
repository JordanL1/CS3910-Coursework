from Pallets import Pallets
from Particle import Particle
from Particle_With_LS import Particle_With_LS

class Swarm:
    def __init__(self, pallet_problem : Pallets, swarm_size : int, iterations : int, is_local_initialised : bool):
        self.swarm_size = swarm_size
        self.iterations = iterations
        self.particles = [None for x in range(swarm_size)]
        self.pallet_problem = pallet_problem
        self.gbest = self.pallet_problem.generate_random_solution()
        self.gbest_cost = self.pallet_problem.evaluate_cost(self.gbest)

        # Create particles

        if not is_local_initialised:
            for i in range(self.swarm_size):
                self.particles[i] = Particle(self.pallet_problem, self.pallet_problem.generate_random_solution())
        else:
            for i in range(self.swarm_size):
                self.particles[i] = Particle_With_LS(self.pallet_problem, self.pallet_problem.generate_random_solution())

    def swarm_search(self):
        for i in range(self.iterations):
            for j in range(len(self.particles)):
                pbest = self.particles[j].update_particle(self.gbest)
                pbest_cost = self.pallet_problem.evaluate_cost(pbest)

                if pbest_cost < self.gbest_cost:
                    self.gbest = pbest
                    self.gbest_cost = pbest_cost

        #print(f"Best found by swarm search: {self.gbest} costing {self.gbest_cost}")
        return [self.gbest, self.gbest_cost]