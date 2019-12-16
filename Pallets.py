import random
import math
import time

class Pallets:
    """
    Represents an instance of the pallet problem and provides the functionality required to
    generate and evaluate valid solutions.
    """
    def __init__(self, file_name):
        """
        Initialise an instance of the pallet problem with data from a file.

        Parameters:
        file_name: a string specifying the location of a CSV file which contains one or more days (as rows) with their known demand followed by estimates
        """
        self.days = self.get_data_from_file(file_name)

    def evaluate_cost(self, weights):
        """
        Evaluate the average estimation error across a list of days for the pallet problem.

        Given a list of 13 weights, calculate the average error in estimating demand when these weights are
        combined, in list order, with the 13 demand measurements for each day, over all days included
        in the data provided.

        Parameters:
        weights: a list containing 13 floats to be combined with the day's demand estimates
        """
        costs = []
        for day in self.days:
            costs.append(self.evaluate_cost_for_one_day(day, weights))
        
        return sum(costs) / len(self.days)

    def evaluate_cost_for_one_day(self, day: list, weights: list):
        """
        Evaluate the estimation error for one day when combining the day's estimates with a set of 13 weights.

        Given one day, consisting of the known demand for the day followed by 13 demand measurements for that
        day, evaluate the error in estimating demand by combining the supplied 13 weights, in list order, with the demand
        measurements and then calculating the difference between the resulting estimation and the known demand.

        Parameters:
        day: a list containing the known demand at the end of the day followed by 13 demand estimates
        weights: a list containing 13 floats to be combined with the day's demand estimates
        """
        weighted_values = []

        for i in range(13):
            weighted_values.append(weights[i] * day[i+1])
        
        estimate = sum(weighted_values)
        
        return abs(estimate - day[0])

    def generate_random_solution(self, lower = -1.0, upper = 1.0):
        """
        Return a random solution to the pallet problem consisting of a list of 13 values.

        Generate a list of 13 random floating point values, where lower <= value <= upper, representing a possible solution to the
        pallet demand problem.

        Parameters:
        iterations: the number of solutions to be generated
        lower (optional): the lower bound above which each weight is generated. Default -1.0
        upper (optional): the upper bound below which each weight is generated. Default 1.0
        """
        params = []

        for i in range(13):
            params.append(random.uniform(lower, upper))

        return params


    def get_data_from_file(self, file_name):
        """ 
        Load data for the pallet problem from a CSV file.

        Given the name of a CSV file containing data for the pallets problem, return a list *days*
        of days. Each day is a list consisting of the known demand at the end of the day (index 0) followed
        by 13 demand measurements (indices 1-13).

        Parameters:
        file_name: a string specifying the location of a CSV file which contains one or more days (as rows) with their known demand followed by estimates
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

    def random_search(self, iterations, lower = -1.0, upper = 1.0):
        """
        Generate random solutions for the specified number of iterations and return the best found.

        Parameters:
        iterations: the number of solutions to be generated
        lower (optional): the lower bound above which each weight is generated. Default -1.0
        upper (optional): the upper bound below which each weight is generated. Default 1.0

        Returns: the best solution found
        """
        best_cost = math.inf
        best_solution = []

        for i in range(iterations):
            solution = self.generate_random_solution(lower, upper)
            cost = self.evaluate_cost(solution)
            print(f"Solution: {solution} Cost: {cost}")

            if cost < best_cost:
                best_cost = cost
                best_solution = solution

        print(f"Best solution found in {iterations} iterations of random search is: ")
        print(f"{best_solution}")
        print(f"Costing: {best_cost}")

        return best_solution

    
    def timed_random_search(self, run_time, lower = -1.0, upper = 1.0):
        """
        Repeatedly generate random solutions for the specified time period and return the best found.

        Parameters:
        run_time: length of time to search for
        lower (optional): the lower bound above which each weight is generated. Default -1.0
        upper (optional): the upper bound below which each weight is generated. Default 1.0

        Returns: a list containing the cost of the best solution found followed by the solution

        """
        best_cost = math.inf
        best_solution = []

        end_time = time.time() + run_time

        while time.time() < end_time:
            solution = self.generate_random_solution(lower, upper)
            cost = self.evaluate_cost(solution)

            if cost < best_cost:
                best_cost = cost
                best_solution = solution

        return [best_cost, best_solution]


    def iterative_neighbourhood_search(self, solution, iterations):
        """
        Conduct an iterative neighbourhood search on a given solution to find lower-cost solutions.

        Generates a neighbourhood of nearby solutions, evaluates them, then selects the best solution from the current best
        and its neighbourhood. Repeats for the specified number of iterations, using the best solution as the new starting
        point each iteration.

        Parameters:
        solution: a set of 13 weights representing a solution to the pallet problem
        iterations: number of iterations to search for

        Returns: the best solution found
        """
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
        """
        Given a solution, find thirteen neighbours by copying the original solution
        and perturbing the value at index i, for 0 <= i < 13.
        """
        neighbours = []

        for i in range(len(solution)):
            neighbour = solution[:]
            # Perturb value at index i
            neighbour[i] = random.normalvariate(solution[i], 2.0)
            neighbours.append(neighbour)

        return neighbours