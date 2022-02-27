from linecache import cache
from tokenize import Double
import numpy as np


def solve():
    DREAM = 1000000
    TOTALSAVINGS = 0.0
    multiple = input().rstrip().split()
    monthly_income = float(multiple[0])
    monthly_expense = float(multiple[1])
    Taxes = float(multiple[2])
    TaxTime = int(multiple[3])
    UnexpectedExpense = float(multiple[4])
    UnExpenseTime = int(multiple[5])
    
    TimeRemainingfromTax = 0
    TimeRemainingfromExpense = 0
    months = 0
    
    
    #! Algorithm
   
        
    while TOTALSAVINGS <= DREAM:
        TOTALSAVINGS += monthly_income - monthly_expense
        print(TOTALSAVINGS)
        TimeRemainingfromTax += 1
        TimeRemainingfromExpense += 1
        months += 1
        if TimeRemainingfromExpense == UnExpenseTime:
            TOTALSAVINGS -= UnexpectedExpense
            TimeRemainingfromExpense = 0
        if TimeRemainingfromTax == TaxTime:
            TOTALSAVINGS = TOTALSAVINGS - ((monthly_income * TimeRemainingfromTax) * Taxes)
            TimeRemainingfromTax = 0
        

    print(months)
def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: ", end = '')
        solve()
        
main()   