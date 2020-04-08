
#!/bin/bash

# numbers script

for num in {0..100} ; do
        if  (! ((num % 3)) ) && (! ((num % 5)) ); then echo "Cat and Mouse"
	elif (! ((num % 3)) ); then echo "Cat"
	elif (! ((num % 5)) ); then echo "Mouse"
	else echo $num;
fi


done

