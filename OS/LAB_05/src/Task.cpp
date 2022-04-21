#include <bits/stdc++.h>
#include <thread>

using namespace std;

void add(int a, int b)
{
    cout << a + b << endl;
}
void sub(int a, int b)
{
    cout << a - b << endl;
}
void mul(int a, int b)
{
    cout << a * b << endl;
}
void divi(float a, float b)
{
    if (b == 0)
        cout << b << endl;
    else
        cout << a / b << endl;
}

int main()
{
    printf("Enter two interger: ");
    int a, b;
    cin >> a >> b;
    thread t1(add, a, b);
    thread t2(sub, a, b);
    thread t3(mul, a, b);
    thread t4(divi, a, b);

    printf("Addition is: ");
    printf("Deletion is: ");
    printf("Multiplication is: ");
    printf("Division is: ");
    t1.join();
    t2.join();
    t3.join();
    t4.join();
}