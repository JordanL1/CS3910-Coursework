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
            params.append(random.uniform(-10, 10))

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