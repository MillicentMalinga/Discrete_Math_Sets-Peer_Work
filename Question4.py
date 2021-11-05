# Print the purpose to the user and ask user input to form the set A
print('Enter four consecutive number,on after the other to build a set  ')
el1 = int(input('Enter the first number please :'))
el2 = int(input('Enter the second number please :'))
el3 = int(input('Enter the third number please :'))
el4 = int(input('Enter the fourth number please :'))
A = {el1, el2, el3, el4}  # Build set A
print(f'The set A is {A}. ')
# Build the set AxA
AxA = {(el1, el1), (el1, el2), (el1, el3), (el1, el4), (el2, el1), (el2, el2), (el2, el3), (el2, el4), (el3, el1),
       (el3, el2), (el3, el3), (el3, el4), (el4, el1), (el4, el2), (el4, el3), (el4, el4)}
# Ask user to build another Set R
print("You will now enter 10 number  for creating a nested list in a form : [[a, b],[c, d],[e, f],[g, h]]")
a = int(input('Enter the first number please :'))
b = int(input('Enter the second number please :'))
c = int(input('Enter the third number please :'))
d = int(input('Enter the fourth number please :'))
e = int(input('Enter the fifth number please :'))
f = int(input('Enter the sixth number please :'))
g = int(input('Enter the seventh number please :'))
h = int(input('Enter the  number please :'))
i = int(input('Enter the number please :'))
j = int(input('Enter the last number please :'))

R = {(a, b), (c, d), (e, f), (g, h), (i, j)}  # Build Set R
print(f"The set R is {R}.")

#  Define a function which returns True if a relation R on set A is reflexive, False otherwise.


def reflexive(R, A):
    for a in A:
        if (a, a) not in R:
            return False
    return True
#  Define a function which returns True if a relation R on set A is symmetric, False otherwise.


def symmetric(R, A):
    for a, b in R:
        if (b, a) not in R:
            return False
    return True

# Define a function which returns True if a relation R on set A is transitive, False otherwise.


def transitive(R, A):
    for a in A:
        for b in A:
            if (a, b) in R:
                for c in A:
                    if (b, c) in R and (a, c) not in R:
                        return False
    return True
# Define functions to print the wrong element if the reflexive function is False


def print_reflexive(R, A):
    for a in A:
        if (a, a) not in R:
            print(f"R is not reflexive: {a}")
    return
# Define functions to print the wrong element if the symmetric function is False


def print_sym(R, A):
    for a, b in R:
        if (b, a) not in R:
            print(f'R is not symmetric : {(b, a)}')
    return

# Define functions to print the wrong element if the transitive function is False


def print_trans(R, A):
    for a in A:
        for b in A:
            if (a, b) in R:
                for c in A:
                    if (b, c) in R and (a, c) not in R:
                        print(f'R is not transitive :{a, b, c}')
    return


if R.issubset(AxA) is True:    # verify if R is a subset of A
    print('R is a set.\nR is a subset of AxA') # will be printed if R is a subset of A
# Otherwise the else will run
else:
    print('R is a set.\nR is not a subset of AxA  because the following element is in R but not in AxA: ')
    print(R.difference(AxA))
    print("R is not a relation on A")
    exit()  # exit the program
# Set up conditions to check if the different function are true or not, then print  related information.

if symmetric(R, A) is True:
    print('R is  reflexive')
else:
    print_reflexive(R, A)
if symmetric(R, A) is True:
    print('R is symmetric')
else:
    print_sym(R, A)
if transitive(R, A) is True:
    print('R is transitive')
else:
    print_trans(R, A)
