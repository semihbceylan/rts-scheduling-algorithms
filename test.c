#include <pthread.h>
#include <stdio.h>

void *thread_function(void *arg) {
    printf("Hello from thread!\n");
    return NULL;
}

int main() {
    pthread_t thread;

    // Create a thread
    pthread_create(&thread, NULL, thread_function, NULL);

    // Wait for the thread to finish
    pthread_join(thread, NULL);

    printf("Thread has finished.\n");
    return 0;
}
