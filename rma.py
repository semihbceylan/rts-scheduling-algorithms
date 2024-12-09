import math

class Task:
    def __init__(self, name, computation_time, period):
        self.name = name
        self.computation_time = computation_time
        self.period = period
        self.deadline = period
        self.priority = 0

def rate_monotonic(tasks):
    tasks.sort(key=lambda x: x.period)
    for idx, task in enumerate(tasks):
        task.priority = idx + 1
    return tasks

tasks = [Task('T1', 1, 5), Task('T2', 2, 10), Task('T3', 1, 15)]
scheduled_tasks = rate_monotonic(tasks)

for task in scheduled_tasks:
    print(f'Task: {task.name}, Computation Time: {task.computation_time}, Period: {task.period}, Priority: {task.priority}')
