
#!/bin/bash

# numbers script

c=0
c1=0
c2=0
c3=0
for num in {0..100} ; do
	num_factor=`factor $num|wc -w`
	if [ $num_factor -eq 2 ]; then echo "Dog" && c3=$(($c3+1))
        elif  (! ((num % 3)) ) && (! ((num % 5)) ); then echo "Cat and Mouse" && c=$(($c+1))
	elif (! ((num % 3)) ); then echo "Cat" && c1=$(($c1+1))
	elif (! ((num % 5)) ); then echo "Mouse" && c2=$(($c2+1))
	else echo $num;
fi

done

echo "The total number of Cat and Mouse is $c!"
echo "The total number of Cat's is $c1!"
echo "The total number of Mice is $c2!"
echo "The total number of Dogs is $c3!"

