from timeit import timeit, repeat
from hill_climbing import *
import random
import numpy as np

N = int(input('Enter number of Queens: '))
hill_climbing_times_list = []
hill_climbing_nodes_list = []
hill_climbing_solved_list = []

sideways_climbing_times_list = []
sideways_nodes_list = []
sideways_solved_list = []

restarts_times_list = []
restarts_nodes_list = []
restarts_solved_list = []

for i in range(100):
    problem = NQueensProblem(N, tuple(random.choice(range(N)) for _ in range(N)))
    hill_climbing_time = timeit('hill_climbing_instrumented(problem)',
                                'from __main__ import hill_climbing_instrumented,problem',
                                number=1)
    sideways_time = timeit('hill_climbing_sideways(problem,10)', 'from __main__ import hill_climbing_sideways,problem',
                           number=1)
    restarts_time = timeit('hill_climbing_random_restart(problem,10)',
                           'from __main__ import hill_climbing_random_restart,problem',
                           number=1)
    hill = hill_climbing_instrumented(problem)
    sideways = hill_climbing_sideways(problem, 10)
    restarts = hill_climbing_random_restart(problem, 10)

    hill_climbing_times_list.append(hill_climbing_time)
    sideways_climbing_times_list.append(sideways_time)
    restarts_times_list.append(restarts_time)

    hill_climbing_nodes_list.append(hill['expanded'])
    sideways_nodes_list.append(sideways['expanded'])
    restarts_nodes_list.append(restarts['expanded'])

    hill_climbing_solved_list.append(hill['solved'])
    sideways_solved_list.append(sideways['solved'])
    restarts_solved_list.append(restarts['solved'])

print("Hillclimbing-----------------------------------------------")
print("AVG Nodes: ", np.mean(hill_climbing_nodes_list))
print("Std Nodes: ", np.std(hill_climbing_nodes_list))
print("AVG Time: ", np.mean(hill_climbing_times_list))
print("Std Time: ", np.std(hill_climbing_times_list))
hill_sovled=hill_climbing_solved_list.count(True)/100*100
print("Probability of solving: ",hill_sovled,"%")

print("Hillclimbing_Sideways-----------------------------------------------")
print("AVG Nodes: ", np.mean(sideways_nodes_list))
print("Std Nodes: ", np.std(sideways_nodes_list))
print("AVG Time: ", np.mean(sideways_climbing_times_list))
print("Std Time: ", np.std(sideways_climbing_times_list))
sovled=sideways_solved_list.count(True)/100*100
print("Probability of solving: ",sovled,"%")
print()

print("Hillclimbing_Restarts-----------------------------------------------")
print("AVG Nodes: ", np.mean(restarts_nodes_list))
print("Std Nodes: ", np.std(restarts_nodes_list))
print("AVG Time: ", np.mean(restarts_times_list))
print("Std Time: ", np.std(restarts_times_list))
sovled=restarts_solved_list.count(True)/100*100
print("Probability of solving: ",sovled,"%")
print()