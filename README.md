# opti

Scheduling jobs on unrelated machines.
 
We are given 24 jobs. In the table below, the processsing times p(i,j) are given: The execution
time for job j is p(i,j), if it is processed by machine Mi.

i 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24

M1 1 8 3 4 3 1 6 5 3 1 2 3 1 2 3 4 3 2 2 5 2 1 2 3

M2 2 1 8 5 2 5 1 2 9 1 4 2 3 1 8 9 3 1 4 3 3 6 3 1

M3 5 4 4 2 8 4 4 6 1 8 2 8  5 6 6 1 3 3 4 1 1 8 2 8

Any machine can process at most one job at any time, preemption is not allowed. Determine the
optimal schedule, minimizing the makespan (the finishing time of the last job should be as small as
possible).

Solution uses list scheduling, and local search as a metaheuristic method to solve this problem.
