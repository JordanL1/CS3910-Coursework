import statistics
import time
from Swarm import Swarm
from Pallets import Pallets

FILE = "data/cwk_train.csv"

pallet_prob = Pallets(FILE)
# 
non_ls = []
using_ls = []
start = time.time()
for i in range(10):
    swarm = Swarm(pallet_prob,60,100,False)
    non_ls.append(swarm.swarm_search()[1])
elapsed_non_lsi = time.time() - start

start = time.time()
for i in range(10):
    swarm = Swarm(pallet_prob,30,100,True)
    using_ls.append(swarm.swarm_search()[1])
elapsed_lsi = time.time() - start

print(f"Results with local search initialisation: {using_ls}. Mean result: {statistics.mean(using_ls)}. Time taken: {elapsed_lsi}")
print(f"Results without local search initialisation: {non_ls}. Mean result: {statistics.mean(non_ls)}. Time taken: {elapsed_non_lsi}")