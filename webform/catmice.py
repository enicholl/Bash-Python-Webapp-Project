# Code for outputting the list of numbers in the users chosen range, with dog, cat, mouse and cat&mouse replaced in
# where required


def cat_mouse(player_number=100):  # default number 100 if none selected by user
    results = []  # for every number in the players range, the outcome is appended to this results list to be displayed
    for x in range(int(player_number) + 1):  # loops over every number up to and including the users chosen number
        prime = True
        for p in range(2, x):  # identifies which numbers ARE NOT prime and changes boolean "prime" to false
            if x % p == 0:
                prime = False
        if (x == 1) or (x == 0):  # ensures that 0 and 1 are not included as prime numbers
            prime = False
            results.append("{}".format(x))
        elif prime:  # saves prime numbers with the value dog
            results.append("Dog")  # adds dog to the results list
        elif (x % 5 == 0) and (x % 3 == 0):  # saves number divisible by 5 and 3 with value cat and mouse
            results.append("Cat and Mouse")  # adds cat and mouse to the results list
        elif x % 3 == 0:  # saves number divisible by 3 with value cat
            results.append("Cat")  # adds cat to the results list
        elif x % 5 == 0:  # saves number divisible by 5 with value mouse
            results.append("Mouse")  # adds mouse to the results list
        else:
            results.append("{}".format(x))  # else number itself is added to the results list
        x += 1  # moves to the next number in the range

    return results  # returns full list of results up to and including the number chosen by the user

