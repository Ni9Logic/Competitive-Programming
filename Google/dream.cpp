#include <bits/stdc++.h>
using namespace std;

void solve()
{
    const int DREAM = 1000000;
    float TOTALSAVINGS = 0;
    float monthly_income, monthly_expense, Taxes, TaxTime, UnexpectedExpense, UnExpenseTime;
    cin >> monthly_income >> monthly_expense >> Taxes >> TaxTime >> UnexpectedExpense >> UnExpenseTime;

    int TimeRemainingfromTax = 0, TimeRemainingfromExpense = 0, months = 0;
    while (TOTALSAVINGS <= DREAM)
    {
        TOTALSAVINGS += monthly_income - monthly_expense;

        TimeRemainingfromTax++;
        TimeRemainingfromExpense++;
        months++;

        if (TimeRemainingfromExpense == UnExpenseTime)
        {
            TOTALSAVINGS = TOTALSAVINGS - UnexpectedExpense;
            TimeRemainingfromExpense = 0;
        }
        if (TimeRemainingfromTax == TaxTime)
        {
            TOTALSAVINGS = TOTALSAVINGS - ((monthly_income * TimeRemainingfromTax) * Taxes);
            TimeRemainingfromTax = 0;
        }
    }
    cout << months << endl;
}

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
}