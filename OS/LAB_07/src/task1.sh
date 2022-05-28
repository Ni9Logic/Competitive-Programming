echo "How many units have you consumed?"
read consumed_units
below_three=2
above_three=5
above_five=7
if (($consumed_units <= 300))
then
echo "Your electricity bill is" `expr $consumed_units \* $below_three`
elif (($consumed_units > 300 && $consumed_units <= 500))
then
echo "Your electric bill is" `expr $consumed_units \* $above_three`
else
echo "Your electric bill is" `expr $consumed_units \* $above_five`
fi