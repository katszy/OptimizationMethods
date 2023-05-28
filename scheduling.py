import random
import copy

def list_scheduling(process_times):
    num_machines = len(process_times)
    
    # Initialize the schedule and completion times
    schedule = [[] for _ in range(num_machines)]
    completion_times = [0] * num_machines
    
    # Iterate over columns
    jobs=  []
    for j in range(len(process_times[0])):
        column = []
        # Iterate over rows
        for i in range(len(process_times)):
            column.append(process_times[i][j])
        jobs.append(column)
        
    machine_finish_time = [0,0,0] #corresponts to M1,M2,M3  
    # Iterate over each job and assign it to a machine with the minimum completion time
    for job in (jobs):
        min_completion_time = float('inf')
        min_machine = None
        tmp_machine_finish_time = list(machine_finish_time)
        for machine in range(num_machines):
            if tmp_machine_finish_time[machine] + job[machine][1] < min_completion_time:
                    min_machine = machine
                    min_completion_time = machine_finish_time[machine] + job[machine][1]
                    tmp_machine_finish_time[machine] += job[machine][1]
        machine_finish_time[min_machine] = tmp_machine_finish_time[min_machine]
        completion_times[min_machine] += job[min_machine][1]
        schedule[min_machine].append(job[machine][0])
          
    return schedule, max(machine_finish_time)

#making 2 random number (the 2 number cant be the same)
def make_two_rand_int(process_times):

  jobs_indexes = len(process_times[0]) - 1
  first = int(random.randint(0,jobs_indexes))

  numbers = list(range(0, jobs_indexes + 1))
  numbers.remove(first)
  second = random.choice(numbers)
  return first,second

# Print the resulting schedule and makespan
def print_result(result_schedule,result_makespan):
  print("Schedule:")
  for machine, jobs in enumerate(result_schedule):
      print(f"Machine {machine+1}: {jobs}")
  print("Makespan:", result_makespan)

def permutation_swap(process_times, calculated_schedule,calculated_makespan, recalculations_num):
  better_solution = 0
  original_makespan = calculated_makespan
  for i in range(recalculations_num):
    saved_process_times = copy.deepcopy(process_times)
    first_element, second_element = make_two_rand_int(saved_process_times)

#swap elements
    for i in saved_process_times:
      i[first_element], i[second_element] = i[second_element], i[first_element]

#calculate jobs with new table
    test_schedule, test_makespan = list_scheduling(saved_process_times)
    
    if(test_makespan < original_makespan):
      better_solution += 1
    
#swap list if it is better solution
    if(test_makespan < calculated_makespan):
      process_times = saved_process_times
      calculated_makespan = test_makespan
      calculated_schedule = test_schedule
    
  
  print("list permutation, swapping, improvement ratio:")
  print(better_solution/recalculations_num*100)
  return calculated_schedule,calculated_makespan

def permutation_tail_to_front(process_times, calculated_schedule,calculated_makespan, recalculations_num):
  better_solution = 0
  original_makespan = calculated_makespan
  for i in range(recalculations_num):
    saved_process_times = copy.deepcopy(process_times)
    jobs_indexes = len(process_times[0]) - 1
    random_int = int(random.randint(0,jobs_indexes-1))
    #swap elements
    for i in saved_process_times:
        i[0:jobs_indexes - random_int +1], i[jobs_indexes - random_int +1:jobs_indexes +1] = i[random_int:jobs_indexes + 1], i[0:random_int]
    test_schedule, test_makespan = list_scheduling(saved_process_times)

    #print("TEST RESULT:::::::::::::::")
    #print_result(test_schedule,test_makespan)
    
    if(test_makespan < original_makespan):
      better_solution += 1

    #swap list if it is better solution
    if(test_makespan < calculated_makespan):
      process_times = saved_process_times
      calculated_makespan = test_makespan
      calculated_schedule = test_schedule

  print("list permutation, tail to the end, improvement ratio:")
  print(better_solution/recalculations_num*100)
  return calculated_schedule,calculated_makespan

def calculate_makespan(sch):
  makespan = 0
  idx = 0
  for m_index, machine in enumerate(sch):
    machine_makespan = 0
    for job in machine:
      job_index = job - 1
      job_processing_time = processing_times[m_index][job_index][1]
      machine_makespan += job_processing_time
      if machine_makespan > makespan:
        makespan = machine_makespan
        idx = m_index
  return makespan, idx
    
def move(ls_schedule, ls_makespan):
  best = ls_makespan
  for i in range(1):
    #choose a machine that deteremines makespan
    sch = copy.deepcopy(ls_schedule)
    makespan, random_machine = calculate_makespan(sch) #random_machine is not actually random!!!  #it's the one that determines the makespan! 
    m = sch[random_machine]
    #choose a random job 
    random_job_index = random.randint(0, len(m) - 1)
    job = processing_times[random_machine][m[random_job_index]-1]
    j = job[0]
    #put it elsewhere to the end, choose machine 
    dest_machine = random_machine
    while (dest_machine==random_machine):
      dest_machine = random.choice([0, 1, 2])
    dest_machine = sch[dest_machine]
    #place job at the end
    m.pop(random_job_index)
    dest_machine.append(j)

    #calculate new makespan 
    makespan, idx = calculate_makespan(sch)
  if makespan <= best:
    best = makespan 
  else:
    sch = ls_schedule
    best = ls_makespan
  return sch,best
  
def swap(ls_schedule, ls_makespan):
  best = ls_makespan
  for i in range(1):
    #choose a machine that deteremines makespan
    sch = copy.deepcopy(ls_schedule)
    makespan, random_machine = calculate_makespan(sch) #random_machine is not actually random!!!  #it's the one that determines the makespan! 
    m = sch[random_machine]
    #choose a random job 
    random_job_index = random.randint(0, len(m) - 1)
    job = processing_times[random_machine][m[random_job_index]-1]
    j = job[0]
    
    #choose a random machine
    dest_machine = random_machine
    while (dest_machine==random_machine):
      dest_machine = random.choice([0, 1, 2])
    md = sch[dest_machine]
    #choose a random job 
    random_job_index_2 = random.randint(0, len(md) - 1)
    job = processing_times[random_machine][md[random_job_index_2]-1]
    jd = job[0]
  
    #swap them
    m[random_job_index] = jd
    md[random_job_index_2] = j

    #calculate new makespan 
    makespan, idx = calculate_makespan(sch)
  if makespan <= best:
    best = makespan  
  else:
    sch = ls_schedule
    best = ls_makespan
  return sch, best
    
# Define the processing time table
processing_times = [
    [[1,1], [2,8], [3,3], [4,4], [5,3], [6,1], [7,6], [8,5], [9,3], [10,1], [11,2], [12,3], [13,1], [14,2], [15,3], [16,4], [17,3], [18,2], [19,2], [20,5], [21,2], [22,1], [23,2], [24,3]],
    [[1,2], [2,1], [3,8], [4,5], [5,2], [6,3], [7,1], [8,2], [9,9], [10,1], [11,4], [12,2], [13,3], [14,1], [15,8], [16,9], [17,3], [18,1], [19,4], [20,3], [21,3], [22,6], [23,3], [24,1]],
    [[1,5], [2,4], [3,4], [4,2], [5,8], [6,4], [7,4], [8,6], [9,1], [10,8], [11,2], [12,8], [13,5], [14,6], [15,6], [16,1], [17,3], [18,3], [19,4], [20,1], [21,1], [22,8], [23,2], [24,8]]
]

# Run the list scheduling algorithm
ls_schedule, ls_makespan = list_scheduling(processing_times)
print_result(ls_schedule, ls_makespan)
print("__________________________________")

#first possibility: move and swap
sch = ls_schedule
makespan = ls_makespan 
for i in range(2000):
  if random.random() < 0.5:
    sch, makespan = move(sch, makespan)
  else: 
    sch, makespan = swap(sch, makespan)
print("SWAP AND MOVE:")
print_result(sch,makespan)
print("__________________________________")

#second possibility: permutating the list 
# Run the list scheduling algorithm
ls_schedule, ls_makespan = list_scheduling(processing_times)
schedule, makespan =permutation_swap(processing_times, ls_schedule, ls_makespan, 2000)
print("LIST PERMUTATION, SWAPPING:")
print_result(schedule,makespan)
print("__________________________________")
schedule, makespan = permutation_tail_to_front(processing_times, ls_schedule, ls_makespan, 2000)
print("LIST PERMUTATION, TAIL TO FRONT:")
print_result(schedule,makespan)