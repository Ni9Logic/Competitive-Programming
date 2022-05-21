#include <bits/stdc++.h>
using namespace std;

int main()
{
    printf("Enter an integer: ");
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
        printf("%d x %d = %d\n", n, i, n * i);
}