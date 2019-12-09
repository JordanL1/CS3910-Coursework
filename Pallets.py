import random

class Pallets:
    def __init__(self, file_name):
        self.days = self.get_data_from_file(file_name)

    def evaluate_cost(self, weights):
        costs = []
        for day in self.days:
            costs.append(self.evaluate_cost_for_one_day(day, weights))
        
        return sum(costs) / len(self.days)

    def evaluate_cost_for_one_day(self, day, weights):
        weighted_values = []

        for i in range(13):
            weighted_values.append(weights[i] * day[i+1])
        
        estimate = sum(weighted_values)
        
        return abs(estimate - day[0])

    def generate_random_solution(self):
        params = []

        for i in range(13):
            params.append(random.uniform(-1, 1))

        return params



    def get_data_from_file(self, file_name):
        """ Given a CSV filename, return a dictionary mapping a city name or ID
        to a tuple containing its 2D coordinates.
        """
        csv = open(file_name, 'r')
        days = []
        for line in csv:
            day = line.rstrip().split(",")
            for i in range(len(day)):
                day[i] = float(day[i])
            days.append(day)   
        print(f"Data from file: {days}")
        return days

    def random_search(self, iterations):
        best_cost = 99999
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
        """Given a solution, find thirteen neighbours where each neighbour has
        one value in the list perturbed."""
        neighbours = []

        for i in range(len(solution)):
            neighbour = solution[:]
            # Perturb value at index i
            neighbour[i] = random.normalvariate(solution[i], 2.0)
            neighbours.append(neighbour)

        return neighbours