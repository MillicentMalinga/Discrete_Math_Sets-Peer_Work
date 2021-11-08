#lines 2 to 7 ask the user for input for the lists
x0 = int(input("Enter the first for the first list\n"))
x1 = int(input("Enter the second number for the first list\n"))
x2 = int(input("Enter the third number for the first list\n"))
y0 = int(input("Enter the first for the second list\n"))
y1 = int(input("Enter the second for the second list\n"))
y2 = int(input("Enter the third for the second list\n"))

#Lines 10 to 11 creates list from user input
a = [x0, x1, x2]
b = [y0, y1, y2]
#empty dictionary to store the modulus after dividing elements in list b by list a
collective = []
#function that takes the parameter a and b which are lists
def truth_false(a, b):
    #Checking and using every element in each list
    for i in a:
        for p in b:
            #appending the modulus to the dictionary
            collective.append(p%i)
    print(collective)
    #checking if any element in the dictionary is equal to zero
    if any(collective) == 0:
        print("TRUE")
    else:
        print("FALSE")
#calling the function
truth_false(a, b)
