#include <bits/stdc++.h>
using namespace std;

void solve()
{
    char vowels[] = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'};
    string kingdom;
    cin >> kingdom;
    bool met = false;
    for (auto &i : vowels)
        if (kingdom[kingdom.size() - 1] == i)
        {
            met = true;
            break;
        }
    if (kingdom[kingdom.size() - 1] == 'y' or kingdom[kingdom.size() - 1] == 'Y')
        printf("%s is ruled by nobody.\n", kingdom.c_str());
    else if (met)
        printf("%s is ruled by Alice.\n", kingdom.c_str());
    else
        printf("%s is ruled by Bob.\n", kingdom.c_str());
}

int main()
{
    int n;
    cin >> n;
    int i = 1;
    while (n--)
    {
        printf("Case #%d: ", i);
        solve();
        i++;
    }
}