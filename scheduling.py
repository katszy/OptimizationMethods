def list_scheduling(process_times):
    num_machines = len(process_times)
    
    # Initialize the schedule and completion times
    schedule = [[] for _ in range(num_machines)]
    completion_times = [0] * num_machines
    
    # Iterate over columns
    jobs=  []
    for j in range(len(processing_times[0])):
        column = []
        # Iterate over rows
        for i in range(len(processing_times)):
            column.append(processing_times[i][j])
        jobs.append(column)
        
    machine_finish_time = [0,0,0,0] #corresponts to M1,M2,M3,M4    
    # Iterate over each job and assign it to a machine with the minimum completion time
    for idx, job in enumerate(jobs):
        min_completion_time = float('inf')
        min_machine = None
        tmp_machine_finish_time = list(machine_finish_time)
        for machine in range(num_machines):
            if tmp_machine_finish_time[machine] + job[machine] < min_completion_time:
                    min_machine = machine
                    min_completion_time = machine_finish_time[machine] + job[machine]
                    tmp_machine_finish_time[machine] += job[machine]
        machine_finish_time[min_machine] = tmp_machine_finish_time[min_machine]
        completion_times[min_machine] += job[min_machine]
        schedule[min_machine].append(idx+1)
          
    return schedule, max(machine_finish_time)

# Define the processing time table
processing_times = [
    [1, 2, 5, 4, 6, 8, 9, 2, 1, 7, 2, 5, 1, 6, 3],
    [7, 8, 9, 12, 15, 14, 13, 19, 11, 15, 16, 15, 4, 3, 2],
    [10, 12, 15, 3, 7, 16, 11, 23, 12, 10, 19, 10, 8, 7, 6],
    [3, 8, 7, 9, 5, 4, 2, 7, 6, 3, 8, 2, 5, 4, 3]
]

# Run the list scheduling algorithm
schedule, makespan = list_scheduling(processing_times)

# Print the resulting schedule and makespan
print("Schedule:")
for machine, jobs in enumerate(schedule):
    print(f"Machine {machine + 1}: {jobs}")
print("Makespan:", makespan)
