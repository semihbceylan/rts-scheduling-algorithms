#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int id;
	int period;
	int execution_time;
	int remaining_time;
	int deadline;
} Task;

void sort_tasks_by_period(Task tasks[], int n) {
	for (int i = 0; i < n - 1; i++) {
		for (int j = 0; j < n - i - 1; j++) {
			if (tasks[j].period > tasks[j + 1].period) {
				Task temp = tasks[j];
				tasks[j] = tasks[j + 1];
				tasks[j + 1] = temp;
			}
		}
	}
}

void rate_monotonic_scheduling(Task tasks[], int n, int hyper_period) {
	for (int time = 0; time < hyper_period; time++) {
		int task_to_run = -1;
		for (int i = 0; i < n; i++) {
			if (time % tasks[i].period == 0) {
				tasks[i].remaining_time = tasks[i].execution_time;
				tasks[i].deadline = time + tasks[i].period;
			}
			if (tasks[i].remaining_time > 0 && (task_to_run == -1 || tasks[i].period < tasks[task_to_run].period)) {
				task_to_run = i;
			}
		}
		if (task_to_run != -1) {
			tasks[task_to_run].remaining_time--;
			printf("Time %d: Task %d is running\n", time, tasks[task_to_run].id);
		} else {
			printf("Time %d: Idle\n", time);
		}
	}
}

int main() {
	Task tasks[] = {
		{1, 3, 1, 0, 0},
		{2, 5, 2, 0, 0},
		{3, 7, 2, 0, 0}
	};
	int n = sizeof(tasks) / sizeof(tasks[0]);
	int hyper_period = 15; // Example hyper-period

	sort_tasks_by_period(tasks, n);
	rate_monotonic_scheduling(tasks, n, hyper_period);

	return 0;
}