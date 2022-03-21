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
            if (counter == 1)
            {    
                counter++;
                index.push_back(i);
                i += 1;
            }
            if (counter == 2)
            {
                counter++;
                index.push_back(i);
                i += 2;
            }
            if (counter == 3){
                counter++;
                index.push_back(i);
                i += 3;
            }
            if (counter == 4){
                counter++;
                index.push_back(i);
                i += 4;
            }
            if (counter == 5){
                i += 5;
                counter++;
                index.push_back(i);
            }
        }

        for (int i = 0; i < index.size(); i++)
            cout << index[i] << " ";
        cout << endl;
    }
}