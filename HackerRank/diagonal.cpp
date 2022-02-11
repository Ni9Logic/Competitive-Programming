#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int arr[n][n];

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> arr[i][j];

    int d1 = 0;
    int d2 = 0;

    for (int i = 0; i < n; i++)
    {
        d1 += arr[i][i];
        d2 += arr[i][n - i - 1];
    }
    cout << abs(d1 - d2) << endl;
}