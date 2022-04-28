#include <bits/stdc++.h>
#include <thread>

using namespace std;

void fun()
{
    printf("Hello\n");
    return;
}

int main()
{
    thread t1(fun);
    cout << t1.get_id() << endl;
    t1.join();
}