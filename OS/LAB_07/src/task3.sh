i=1
max=0

while [ $i -le 3 ]
do
  echo "Enter number "$i": "
  read num
  if [ $i -eq 1 ]  
  then
      max=$num
  else  
      if [ $num -gt $max ]
      then
        max=$num
      fi
  fi
  i=$((i + 1)) #? Increments.
done

echo "Maximum number is: " $max