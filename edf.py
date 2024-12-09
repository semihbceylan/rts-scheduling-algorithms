class Task:
    def __init__(self, name, computation_time, period, deadline):
        self.name = name
        self.computation_time = computation_time
        self.period = period
        self.deadline = deadline

def earliest_deadline_first(tasks):
    tasks.sort(key=lambda x: x.deadline)
    return tasks

tasks = [Task('T1', 1, 5, 5), Task('T2', 2, 10, 8), Task('T3', 1, 15, 12)]
scheduled_tasks = earliest_deadline_first(tasks)

for task in scheduled_tasks:
    print(f'Task: {task.name}, Computation Time: {task.computation_time}, Period: {task.period}, Deadline: {task.deadline}')
