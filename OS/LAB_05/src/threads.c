#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void *myThread(void *vargp)
{
    sleep(1);
    printf("Process thread is being created\n");
    return NULL;
}
int main()
{
    pthread_t thread_1;
    printf("Before creation of the thread\n");
    pthread_create(&thread_1, NULL, myThread, NULL);
    pthread_join(thread_1, NULL);
    printf("After creation of the thread\n");
    exit(0);
}