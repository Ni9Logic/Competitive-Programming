#include <bits/stdc++.h>
using namespace std;

#define ll long long
void solve()
{
    ll cash, cost, modulus;
    cin >> cash >> cost >> modulus;
    ll wrappers = cash / cost;

    if (wrappers % modulus == 0)
    {
        cout << wrappers + 1 << endl;
        return;
    }
    while (wrappers % modulus == 1)
    {
        wrappers++;
        if (wrappers % modulus == 0)
        {
            cout << wrappers + 1 << endl;
            return;
        }
    }
    if (wrappers % modulus == wrappers)
    {
        while (!wrappers % modulus == 0)
        {
            wrappers++;
            if (wrappers % modulus == 0)
            {
                cout << wrappers - 1 << endl;
                return;
            }
        }
    }
}

int main()
{
    int n;
    cin >> n;
    while (n--)
        solve();
}