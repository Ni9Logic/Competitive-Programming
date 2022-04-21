#include <bits/stdc++.h>
#include <thread>

using namespace std;

void func()
{
    printf("Inside the thread\n");
}
void fun()
{
    thread nthread(func);
    printf("This line will print before the thread terminates...\n");
    this_thread::get_id() == nthread.get_id()
        ? printf("Threads are equal\n")
        : printf("Threads are not equal\n");

    nthread.join();
    printf("This line will print after the thread terminates...\n");
}

int main()
{
    fun();
    return 0;
}