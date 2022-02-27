#include <bits/stdc++.h>
using namespace std;

void solve()
{
    const int DREAM = 1000000;

    float TOTALSAVINGS = 0;
    float
        monthly_income = 0.0,
        monthly_expense = 0.0,
        Taxes = 0.0,
        UnexpectedExpense = 0.0;

    auto TimeRemainingfromTax = 0,
         TimeRemainingfromExpense = 0;

    auto months = 0,
         UnExpenseTime = 0,
         TaxTime = 0;

    cout << setprecision(2);
    cin >> monthly_income >> monthly_expense >> Taxes >> TaxTime >> UnexpectedExpense >> UnExpenseTime;

    for (TOTALSAVINGS = 0; TOTALSAVINGS <= DREAM; TOTALSAVINGS += monthly_income - monthly_expense)
    {
        TimeRemainingfromTax++;
        TimeRemainingfromExpense++;
        months++;
        cout << TOTALSAVINGS << endl;
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
        printf("Case #%d: ", i + 1);
        solve();
    }
}