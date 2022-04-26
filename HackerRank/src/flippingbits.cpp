#include <bits/stdc++.h>
using namespace std;

int main()
{
    long limit = 4294967295;
    int n;
    cin >> n;
    while (n--)
    {
        long t;
        cin >> t;
        cout << abs(limit - t) << endl;
    }
}