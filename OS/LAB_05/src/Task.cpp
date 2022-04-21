#include <bits/stdc++.h>
#include <thread>

using namespace std;

int add(int a, int b)
{
    return a + b;
}
int sub(int a, int b)
{
    return a - b;
}
int mul(int a, int b)
{
    return a * b;
}
float division(float a, float b)
{
    if (b == 0)
        return b;
    else
        return a / b;
}

int main()
{
    printf("Enter two interger: ");
    int a, b;
    cin >> a >> b;
    thread t1(add, a, b);
    thread t2(sub, a, b);
    thread t3(mul, a, b);
    thread t4(division, a, b);

    printf("Addition is: ");
    printf("\nDeletion is: ");
    printf("\nMultiplication is: ");
    printf("\nDivision is: ");
    t1.join();
    t2.join();
    t3.join();
    t4.join();
    cout << endl;
}