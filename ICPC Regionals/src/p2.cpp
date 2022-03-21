#include <bits/stdc++.h>
using namespace std;
#define int_64t int

int main()
{
    int a, b;
    cin >> a >> b;
    int a1, b1;
    cin >> a1 >> b1;

    vector<pair<int, int>> customer_demands;
    for (int i = 0; i < a; i++)
    {
        int a, b;
        cin >> a >> b;
        customer_demands.push_back(make_pair(a, b));
    }

    int counter = 0;
    vector<int> index;
    for (int i = 0; i < 6; i++)
    {
        if (b > 0)
        {
            int order = customer_demands[i].first + customer_demands[i].second;
            int required = a1 + b1;
            if (order > required)
                continue;
            else
            {
                b--;
                counter++;
                index.push_back(i + 1);
            }
        }
    }

    for (int i = 0; i < (int)index.size(); i++)
        for (int j = i + 1; j < (int)index.size(); j++)
        {
            int add1 = customer_demands[index[i]].first + customer_demands[index[i]].second;
            int add2 = customer_demands[index[j]].first + customer_demands[index[j]].second;
            if (add1 < add2)
            {
                int temp = 0;
                temp = index[i];
                index[i] = index[j];
                index[j] = temp;
            }
        }

    cout << counter << endl;
    for (int i = 0; i < (int)index.size(); i++)
    {
        cout << index[i];
        if (i != (int)index.size() - 1)
            cout << " ";
    }
    cout << endl;
}