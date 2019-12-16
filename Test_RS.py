import statistics
import time
import csv
from Pallets import Pallets

FILE = "data/cwk_train.csv"
OUTPUT = "data/test_results_random_search.csv"

fieldnames_rs = ['Runs','Run Time', 'Lower Bound', 'Upper Bound', 'Mean', 'Standard Deviation', 'Costs', 'Solutions']

def test_random_search(runs: int, run_time: int, lower = -1.0, upper = 1.0):
    pallet_prob = Pallets(FILE)
    
    results = []
    result_costs = []

    for i in range(runs):
        result = pallet_prob.timed_random_search(run_time, lower, upper)
        results.append(result[1])
        result_costs.append(result[0])

    mean = statistics.mean(result_costs)
    stdev = statistics.stdev(result_costs)

    with open(OUTPUT, mode='a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames_rs)
        writer.writerow({'Runs' : runs, 'Run Time' : run_time, 'Lower Bound' : lower, 'Upper Bound' : upper, 'Mean' : mean, 'Standard Deviation' : stdev, 'Costs' : result_costs, 'Solutions' : results})

    print("Test Complete!")


test_random_search(100, 15)
test_random_search(100, 60)

test_random_search(100, 15, -2.0, 2.0)
test_random_search(100, 15, -5.0, 5.0)
test_random_search(100, 15, -10.0, 10.0)
test_random_search(100, 15, -30.0, 30.0)

