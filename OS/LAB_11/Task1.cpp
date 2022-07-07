#include <iostream>
using namespace std;

void find_wt(int processes[], int n, int bt[], int wt[])
{
    wt[0] = 0;
    for (int i = 0; i < n; i++)
        wt[i] = bt[i - 1] + wt[i - 1];
}

int main()
{
}