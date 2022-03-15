#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    getline(cin, s);
    int n = s.size();
    
    int left = floor(sqrt(n));
    int right = ceil(sqrt(n));

    if (left * right < n)
        min(left, right) ? left++ : right++;

    char arr[left][right];
    int stringindex = 0;
    for (int i = 0; i < left; i++)
        for (int j = 0; j < right; j++)
        {
            arr[i][j] = s[stringindex];
            stringindex++;
        }

    for (int j = 0; j < right; j++)
    {
        for (int i = 0; i < left; i++)
            cout << arr[i][j];
        if (j == right - 1)
            continue;
        cout << " ";
    }
}