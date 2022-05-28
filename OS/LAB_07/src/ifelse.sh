echo "Enter your marks"
read Marks
a=80
b=70
c=60
d=50
if [ $Marks > 80 ]
then
    echo "Your grade is A"
elif [ $Marks -gt $b and $Marks -lt $a ]
then
    echo "Your gtade is B"
elif [ $Marks -gt $c and $Marks -lt $b ]
then
    echo "Your grade is C"
elif [ $Marks -gt $d and $Marks -lt $c ]
then    
    echo "Your grade is D"
else    
    echo "Your grade is F"
fi