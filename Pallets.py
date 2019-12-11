import random
import math

class Pallets:
    def __init__(self, file_name):
        self.days = self.get_data_from_file(file_name)

    def evaluate_cost(self, weights):
        """
        Given a list of 13 weights, calculate the average error in estimating demand when these weights are
        combined, in list order, with the 13 demand measurements over for each day, over all days included
        in the data provided.
        """
        costs = []
        for day in self.days:
            costs.append(self.evaluate_cost_for_one_day(day, weights))
        
        return sum(costs) / len(self.days)

    def evaluate_cost_for_one_day(self, day, weights):
        """
        Given one day, consisting of the known demand for the day followed by 13 demand measurements for that
        day, evaluate the error in estimating demand by combining the supplied 13 weights, in list order, with the demand
        measurements and then calculating the difference between the resulting estimation and the known demand.
        """
        weighted_values = []

        for i in range(13):
            weighted_values.append(weights[i] * day[i+1])
        
        estimate = sum(weighted_values)
        
        return abs(estimate - day[0])

    def generate_random_solution(self):
        """
        Generate a list of 13 random floating point values, where -1 <= value <= 1, representing a possible solution to the
        pallet demand problem.
        """
        params = []

        for i in range(13):
            params.append(random.uniform(-1, 1))

        return params


    def get_data_from_file(self, file_name):
        """ Given the name of a CSV file containing data for the pallets problem, return a list *days*
        of days. Each day is a list consisting of the known demand at the end of the day (index 0) followed
        by 13 demand measurements (indices 1-13).
        """
        csv = open(file_name, 'r')
        days = []
        for line in csv:
            day = line.rstrip().split(",")
            for i in range(len(day)):
                day[i] = float(day[i])
            days.append(day)   
        #print(f"Data from file: {days}")
        return days

    def random_search(self, iterations):
        best_cost = math.inf
        best_solution = []

        for i in range(iterations):
            solution = self.generate_random_solution()
            cost = self.evaluate_cost(solution)
            print(f"Solution: {solution} Cost: {cost}")

            if cost < best_cost:
                best_cost = cost
                best_solution = solution

        print(f"Best solution found in {iterations} iterations of random search is: ")
        print(f"{best_solution}")
        print(f"Costing: {best_cost}")

        return best_solution

    def iterative_neighbourhood_search(self, solution, iterations):
        best = solution
        best_cost = self.evaluate_cost(solution)
        #print(f"Initial solution {best} costing {best_cost}")

        for i in range(iterations):
            neighbourhood = self.find_neighbourhood(best)
            best_neighbour = min(neighbourhood, key = lambda n : self.evaluate_cost(n))
            best_neighbour_cost = self.evaluate_cost(best_neighbour)

            #print(f"Best neighbour: {best_neighbour} costing: {best_neighbour_cost}")

            if best_neighbour_cost < best_cost:
                best = best_neighbour
                best_cost = best_neighbour_cost

        #print(f"Best found in {iterations} iterations: {best} Costing: {best_cost}")
        return best


    def find_neighbourhood(self, solution):
        """Given a solution, find thirteen neighbours by copying the original solution
        and perturbing the value at index i, for 0 <= i < 13."""
        neighbours = []

        for i in range(len(solution)):
            neighbour = solution[:]
            # Perturb value at index i
            neighbour[i] = random.normalvariate(solution[i], 2.0)
            neighbours.append(neighbour)

        return neighbours