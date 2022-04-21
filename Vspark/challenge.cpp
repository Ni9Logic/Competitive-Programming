#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

place:
    int i = 0;
    for (int i = 1; i <= n; i++)
        cout << n;

    if (i == n)
        return 0;

    n--;
    i++;
    printf("\n");
    goto place;
}