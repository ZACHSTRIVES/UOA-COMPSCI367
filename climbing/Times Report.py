from timeit import timeit, repeat
from hill_climbing import *
import random
import numpy as np

N = int(input('Enter number of Queens: '))

print("Hillclimbing-----------------------------------------------")
problem1 = NQueensProblem(N, tuple(random.choice(range(N)) for _ in range(N)))
problem2 = NQueensProblem(N, tuple(random.choice(range(N)) for _ in range(N)))
problem3 = NQueensProblem(N, tuple(random.choice(range(N)) for _ in range(N)))
problem4 = NQueensProblem(N, tuple(random.choice(range(N)) for _ in range(N)))
problem5 = NQueensProblem(N, tuple(random.choice(range(N)) for _ in range(N)))
problem6 = NQueensProblem(N, tuple(random.choice(range(N)) for _ in range(N)))
problem7 = NQueensProblem(N, tuple(random.choice(range(N)) for _ in range(N)))
problem8 = NQueensProblem(N, tuple(random.choice(range(N)) for _ in range(N)))
problem9 = NQueensProblem(N, tuple(random.choice(range(N)) for _ in range(N)))
problem10 = NQueensProblem(N, tuple(random.choice(range(N)) for _ in range(N)))

problem_list = [problem1, problem2, problem3, problem4, problem5, problem6, problem7, problem8, problem9, problem10]
t1 = timeit('hill_climbing_instrumented(problem1)', 'from __main__ import hill_climbing_instrumented,problem1',
            number=1)
t2 = timeit('hill_climbing_instrumented(problem2)', 'from __main__ import hill_climbing_instrumented,problem2',
            number=1)
t3 = timeit('hill_climbing_instrumented(problem3)', 'from __main__ import hill_climbing_instrumented,problem3',
            number=1)
t4 = timeit('hill_climbing_instrumented(problem4)', 'from __main__ import hill_climbing_instrumented,problem4',
            number=1)
t5 = timeit('hill_climbing_instrumented(problem5)', 'from __main__ import hill_climbing_instrumented,problem5',
            number=1)
t6 = timeit('hill_climbing_instrumented(problem6)', 'from __main__ import hill_climbing_instrumented,problem6',
            number=1)
t7 = timeit('hill_climbing_instrumented(problem7)', 'from __main__ import hill_climbing_instrumented,problem7',
            number=1)
t8 = timeit('hill_climbing_instrumented(problem8)', 'from __main__ import hill_climbing_instrumented,problem8',
            number=1)
t9 = timeit('hill_climbing_instrumented(problem9)', 'from __main__ import hill_climbing_instrumented,problem9',
            number=1)
t10 = timeit('hill_climbing_instrumented(problem10)', 'from __main__ import hill_climbing_instrumented,problem10',
             number=1)

time_list = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
print("Time Mean:", np.mean(time_list))
print("Time Std:", np.std(time_list))

nodes = []
solve = []
for p in problem_list:
    res = hill_climbing_instrumented(p)
    nodes.append(res['expanded'])
    solve.append(res['solved'])

print("Nodes Mean:", np.mean(nodes))
print("Nodes Std:", np.std(nodes))

num_of_solved = solve.count(True)
print("Probability of solving:", num_of_solved / 10*100, "%")

print("Hillclimbing_Sideways-----------------------------------------------")
t1 = timeit('hill_climbing_sideways(problem1,10)', 'from __main__ import hill_climbing_sideways,problem1',
            number=1)
t2 = timeit('hill_climbing_sideways(problem2,10)', 'from __main__ import hill_climbing_sideways,problem2',
            number=1)
t3 = timeit('hill_climbing_sideways(problem3,10)', 'from __main__ import hill_climbing_sideways,problem3',
            number=1)
t4 = timeit('hill_climbing_sideways(problem4,10)', 'from __main__ import hill_climbing_sideways,problem4',
            number=1)
t5 = timeit('hill_climbing_sideways(problem5,10)', 'from __main__ import hill_climbing_sideways,problem5',
            number=1)
t6 = timeit('hill_climbing_sideways(problem6,10)', 'from __main__ import hill_climbing_sideways,problem6',
            number=1)
t7 = timeit('hill_climbing_sideways(problem7,10)', 'from __main__ import hill_climbing_sideways,problem7',
            number=1)
t8 = timeit('hill_climbing_sideways(problem8,10)', 'from __main__ import hill_climbing_sideways,problem8',
            number=1)
t9 = timeit('hill_climbing_sideways(problem9,10)', 'from __main__ import hill_climbing_sideways,problem9',
            number=1)
t10 = timeit('hill_climbing_sideways(problem10,10)', 'from __main__ import hill_climbing_sideways,problem10',
             number=1)
time_list = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
print("Time Mean:", np.mean(time_list))
print("Time Std:", np.std(time_list))

nodes = []
solve = []
for p in problem_list:
    res = hill_climbing_sideways(p,10)
    nodes.append(res['expanded'])
    solve.append(res['solved'])

print("Nodes Mean:", np.mean(nodes))
print("Nodes Std:", np.std(nodes))

num_of_solved = solve.count(True)
print("Probability of solving:", num_of_solved / 10*100, "%")

print("Hillclimbing_Restart-----------------------------------------------")
t1 = timeit('hill_climbing_random_restart(problem1,10)', 'from __main__ import hill_climbing_random_restart,problem1',
            number=1)
t2 = timeit('hill_climbing_random_restart(problem2,10)', 'from __main__ import hill_climbing_random_restart,problem2',
            number=1)
t3 = timeit('hill_climbing_random_restart(problem3,10)', 'from __main__ import hill_climbing_random_restart,problem3',
            number=1)
t4 = timeit('hill_climbing_random_restart(problem4,10)', 'from __main__ import hill_climbing_random_restart,problem4',
            number=1)
t5 = timeit('hill_climbing_random_restart(problem5,10)', 'from __main__ import hill_climbing_random_restart,problem5',
            number=1)
t6 = timeit('hill_climbing_random_restart(problem6,10)', 'from __main__ import hill_climbing_random_restart,problem6',
            number=1)
t7 = timeit('hill_climbing_random_restart(problem7,10)', 'from __main__ import hill_climbing_random_restart,problem7',
            number=1)
t8 = timeit('hill_climbing_random_restart(problem8,10)', 'from __main__ import hill_climbing_random_restart,problem8',
            number=1)
t9 = timeit('hill_climbing_random_restart(problem9,10)', 'from __main__ import hill_climbing_random_restart,problem9',
            number=1)
t10 = timeit('hill_climbing_random_restart(problem10,10)', 'from __main__ import hill_climbing_random_restart,problem10',
             number=1)
time_list = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
print("Time Mean:", np.mean(time_list))
print("Time Std:", np.std(time_list))

nodes = []
solve = []
for p in problem_list:
    res = hill_climbing_random_restart(p,10)
    nodes.append(res['expanded'])
    solve.append(res['solved'])

print("Nodes Mean:", np.mean(nodes))
print("Nodes Std:", np.std(nodes))

num_of_solved = solve.count(True)

print("Probability of solving:", num_of_solved / 10 *100, "%")