import statistics
import time
import csv
from Swarm import Swarm
from Pallets import Pallets

FILE = "data/cwk_train.csv"

fieldnames = ['Runs', 'LSI', 'Swarm Size','Run Time', 'Cognitive Coefficient', 'Mean', 'Standard Deviation', 'Costs', 'Solutions']

def run_test(runs: int, LSI: bool, swarm_size: int, run_time: int, cog_coefficient = 1.1193):
    pallet_prob = Pallets(FILE)
    swarm = Swarm(pallet_prob, cog_coefficient)
    
    results = []
    result_costs = []

    for i in range(runs):
        if LSI == True:
            result = swarm.timed_swarm_search_with_lsi(swarm_size, run_time)
        else:
            result = swarm.timed_swarm_search(swarm_size, run_time)
        results.append(result[0])
        result_costs.append(result[1])

    mean = statistics.mean(result_costs)
    stdev = statistics.stdev(result_costs)

    with open('data/test_results_training_file.csv', mode='a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'Runs' : runs, 'LSI' : LSI, 'Swarm Size' : swarm_size, 'Run Time' : run_time, 'Cognitive Coefficient' : cog_coefficient, 'Mean' : mean, 'Standard Deviation' : stdev, 'Costs' : result_costs, 'Solutions' : results})

    print("Test Complete!")

# Test different swarm sizes
run_test(100, False, 30, 15)
run_test(100, True, 30, 15)
run_test(100, False, 100, 15)
run_test(100, True, 100, 15)
run_test(100, False, 500, 15)
run_test(100, True, 500, 15)