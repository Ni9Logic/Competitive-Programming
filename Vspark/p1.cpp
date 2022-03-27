#include <iostream>
using namespace std;
int s[1001], v[1001], n;
double t;
int solve(double c);
int main()
{
    double right = 1e9;
    double left = -1e9;
    double common = (right + left) / 2;

    cin >> n >> t;
    for (int i = 0; i <= n - 1; i++)
        cin >> s[i] >> v[i];
    while (right - left >= 1e-9)
        if (solve(common) > 0)
        {
            right = common;
            common = (right + left) / 2;
        }
        else
        {
            left = common;
            common = (right + left) / 2;
        }
    printf("%.9lf\n", common);
}

int solve(double c)
{
    double sum = 0;
    for (int i = 0; i <= n - 1; i++)
        if (v[i] + c <= 0)
            return -1;
        else
            sum += s[i] * 1.0 / (v[i] + c);

    return sum < t ? 1 : -1;
}