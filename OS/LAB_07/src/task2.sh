echo "Enter your salary"
read Salary
echo "Enter your grade"
read Grade
if (($Grade > 15))
then
echo "Your total salary is " `expr $Salary / 2 + $Salary` #This is $Salary / 2 is 50 percent of his salary and this bonous
elif (($Grade <= 15))
then
echo "Your total salary is " `expr $Salary / 4 + $Salary`
fi