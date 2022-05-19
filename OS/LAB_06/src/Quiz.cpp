#include <bits/stdc++.h>
#include <thread>

using namespace std;

int add(int a, int b)
{
    cout << a + b;
    return a + b;
}
int sub(int a, int b)
{
    cout << a - b;
    return a - b;
}
int mul(int a, int b)
{
    cout << a * b;
    return a * b;
}
float division(float a, float b)
{
    if (b == 0)
    {
        cout << b;
        return b;
    }
    else
    {
        cout << a / b;
        return a / b;
    }
}

int main()
{
    printf("Enter two integer: ");
    int a, b;
    cin >> a >> b;

    printf("Addition is: ");
    thread t1(add, a, b);
    t1.join();

    printf("\nDeletion is: ");
    thread t2(sub, a, b);
    t2.join();

    printf("\nMultiplication is: ");
    thread t3(mul, a, b);
    t3.join();

    printf("\nDivision is: ");
    thread t4(division, a, b);
    t4.join();
    cout << endl;
}