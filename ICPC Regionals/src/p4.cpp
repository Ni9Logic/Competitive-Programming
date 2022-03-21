#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    while (n--)
    {
        int a;
        cin >> a;
        cout << a << " ";
        vector<int> index;
        int counter = 1;
        for (int i = 1; i < a; i++)
        {
            cout << i << " ";
            if (counter == 1)
            {
                i += 1;
                counter++;
                index.push_back(i);
            }
            else if (counter == 2)
            {
                i += 2;
                counter = 1;
                index.push_back(i);
            }
        }

        cout << index[index.size() - 1] << endl;
    }
}