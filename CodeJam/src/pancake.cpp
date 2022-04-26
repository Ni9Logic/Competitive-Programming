#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back

void solve()
{
    int maincounter = 0;
    int n;
    cin >> n;

    int same_elements = 0;

    // Logic begins from here!
    deque<ll> pancakes;
    for (int i = 0; i < n; i++)
    {
        int val;
        cin >> val;
        pancakes.push_back(val);
    }

    //! If all the elements are same in the list!
    ll num = pancakes[0];
    for (int i = 0; i < pancakes.size(); i++)
        if (pancakes[i] == num)
            same_elements++;

    if (same_elements == n)
    {
        printf("%d\n", n);
        return;
    }
    else
    {
        //! Rest of the logic!
        vector<ll> last_element;
        for (int i = 0; i < pancakes.size(); i++)
        {
            last_element.pb(min(pancakes.back(), pancakes.front()));
            if (last_element[last_element.size() - 1] > min(pancakes.back(), pancakes.front()) && pancakes.back() < pancakes.front())
            {
                maincounter += 1;
                pancakes.pop_back();
            }
            else
            {
                pancakes.pop_front();
                maincounter += 1;
            }
        }

        cout << maincounter << endl;
    }
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