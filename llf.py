class Task:
    def __init__(self, name, computation_time, period, deadline, arrival_time):
        self.name = name
        self.computation_time = computation_time
        self.period = period
        self.deadline = deadline
        self.arrival_time = arrival_time
        self.laxity = deadline - (arrival_time + computation_time)

#least slack time
def least_laxity_first(tasks):
    tasks.sort(key=lambda x: x.laxity)
    return tasks

tasks = [Task('T1', 1, 5, 5, 0), Task('T2', 2, 10, 8, 0), Task('T3', 1, 15, 12, 0)]
scheduled_tasks = least_laxity_first(tasks)

for task in scheduled_tasks:
    print(f'Task: {task.name}, Computation Time: {task.computation_time}, Period: {task.period}, Deadline: {task.deadline}, Arrival Time: {task.arrival_time}, Laxity: {task.laxity}')
