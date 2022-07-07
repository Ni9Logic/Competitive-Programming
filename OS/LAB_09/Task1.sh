echo "Enter 10 values: "
sum=0
evensum=0
oddsum=0
for ((i=0; i<=10; i++))
do
read array[n]
if (($((array[n] % 2 == 0))))
then
evensum=$((evensum + array[n]))
else
oddsum=$((oddsum + array[n]))
fi
sum=$((sum + array[n]))
done

average=0
echo "Average of all the entered numbers are:" $((sum/10))
echo "Even sum of all the entered numbers are:" $evensum
echo "Odd sum of all the entered numbers are:" $oddsum

