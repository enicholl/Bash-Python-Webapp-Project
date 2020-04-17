# imports sys module to be used to insert variables from index.js file
import sys


# code for returning the total number of mice
def mouse(player_number=100):
    Cat_Mouse = 0  # represents total number of Cat and Mouse
    Cat = 0  # represents total number of Cats
    Mouse = 0  # represents total number of Mice
    Dog = 0  # represents total number of Dogs
    none = 0  # total of all other values
    for x in range(int(sys.argv[1]) + 1):  # loops over every number up to and including the users chosen number
        prime = True
        for p in range(2, x):  # identifies which numbers ARE NOT prime and changes boolean "prime" to false
            if x % p == 0:
                prime = False
        if (x == 1) or (x == 0):  # ensures that 0 and 1 are not included as prime numbers
            prime = False
        elif prime:  # saves prime numbers with the value dog
            Dog = (Dog + 1)  # adds one to total number of dogs
        elif (x % 5 == 0) and (x % 3 == 0):  # saves number divisible by 5 and 3 with value cat and mouse
            Cat_Mouse = (Cat_Mouse + 1)  # adds one to total number of cat and mouse
        elif x % 3 == 0:  # saves number divisible by 3 with value cat
            Cat = (Cat + 1)  # adds one to the total number of cat and mouse
        elif x % 5 == 0:  # saves number divisible by 5 with value mouse
            Mouse = (Mouse + 1)  # adds one to the total number of mice
        else:
            none = (none + 1)  # adds one to the total of none
        x += 1  # moves to the next number in the range

    print(Mouse)  # prints the total number added to variable Mouse

# runs function mouse()
mouse()
