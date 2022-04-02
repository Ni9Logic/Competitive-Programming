#include <bits/stdc++.h>
using namespace std;

#define ll long long

void solve()
{
    int n;
    cin >> n;
    vector<pair<ll, ll>> units(n);

    for (int i = 0; i < n; i++)
        cin >> units[i].first;
    for (int i = 0; i < n; i++)
        cin >> units[i].second;


    
}

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        printf("Case #%d: ", i + 1);
        solve();
    }
}