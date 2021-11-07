"""
Program only makes use of lists and functions related to lists
Program makes use of only basic python functions 
"""
# Ask user to input numbers
print("Lets create list A consisting of numbers")
a = int(input("1:"))
b = int(input("2:"))
c = int(input("3:"))
d = int(input("4:"))
print("Lets create list B consisting of numbers")
e = int(input("1:"))
f = int(input("2:"))
g = int(input("3:"))

# Converts the user input into two lists and program outputs the lists
x = [a, b, c, d]
A = list(x)
y = [e, f, g]
B = list(y)
print("List A:", A)
print("List B:", B)


# Function checks whether there are common elements between both lists
def check(lis1, lis2):
    for item1 in lis1:
        for item2 in lis2:
            if item1 == item2:
                return True
    return False


# An empty set is created
c = []


# Function checks for the set difference between the two sets and appends the result into the empty set c
def set_dif(lis1, lis2):
    for item in lis1:
        if item not in lis2:
            c.append(item)
    print("A - B ==>", c)


# Function to output the cartesian product of the two sets
def cart_prod(lis1, lis2):
    # An empty set is created
    prod = []
    # Values of both lists are appended into the empty set prod
    for item1 in lis1:
        for item2 in lis2:
            prod.append(item1)
            prod.append(item2)
    # Pairs up each item of set 1 to each item of set 2 and outputs the result
    output = [prod[i:i + 2] for i in range(0, len(prod), 2)]
    print("A x B ==>", output)


result = check(A, B)
# Result value here is True and therefore,outputs that the two sets are subsets
if result:
    print("\nB is a subset of A")
    set_dif(A, B)
    cart_prod(A, B)
# Result value here is False and therefore,outputs that the two sets are not subsets
else:
    print("\nB is not a subset of A")
