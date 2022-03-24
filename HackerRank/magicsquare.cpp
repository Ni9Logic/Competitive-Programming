#include <bits/stdc++.h>
using namespace std;

int main()
{
    int matrix[2][2];
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            cin >> matrix[i][j];

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
            cout << matrix[i][j] << " ";
        cout << endl;
    }
}