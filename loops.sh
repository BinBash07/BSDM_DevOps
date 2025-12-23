read -p "Enter a number: " num
sum=0

echo "Multiplication Table of $num"
for i in {1..10}
do
    result=$((num * i))
    echo "$num x $i = $result"
    sum=$((sum + result))
done

echo "Sum of table values = $sum"
