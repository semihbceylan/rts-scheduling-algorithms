class Task:
    def __init__(self, name, computation_time, period, deadline):
        self.name = name
        self.computation_time = computation_time
        self.period = period
        self.deadline = deadline
        self.priority = 0

def deadline_monotonic(tasks):
    tasks.sort(key=lambda x: x.deadline)
    for idx, task in enumerate(tasks):
        task.priority = idx + 1
    return tasks

tasks = [Task('T1', 1, 5, 5), Task('T2', 2, 10, 8), Task('T3', 1, 15, 12)]
scheduled_tasks = deadline_monotonic(tasks)

for task in scheduled_tasks:
    print(f'Task: {task.name}, Computation Time: {task.computation_time}, Period: {task.period}, Deadline: {task.deadline}, Priority: {task.priority}')
