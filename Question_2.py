def set_functions(a, b):
    def subset_check(a, b):
        """

        :param a: Is a set which is to be checked whether or not it contains parameter b
        :param b: Is a set to be checked if it is a subset of a
        :return: Boolean value: True or False
        """
        if isinstance(a, set) and isinstance(b, set):  # checks if the given a, b are actually sets

            print(b.issubset(a))  # returns True or False
        else:
            # makes sure that when a user inputs any other type then the program lets the user know the error
            raise TypeError("a and b should both be sets")

    def cross_product(a, b):
        """
        finds the cross product of a and b
        :param a: set A
        :param b: set B
        :return: cross product which is a list
        """
        s = []
        if isinstance(a, set) and isinstance(b, set):
            if len(a) >= len(b):
                for j in a:
                    for i in b:
                        q = (zip(j, i))
                        s.append(*q)

                for i in s:
                    print(*zip(*i))

            elif len(b) > len(a):
                for j in b:
                    for i in a:
                        q = (zip(j, i))
                        s.append(*q)
                for i in s:
                    print(*zip(*i))
        else:
            raise TypeError("a and b should be sets")

    def dif_in_sets(a, b):
        if isinstance(a, set) and isinstance(b, set):
            print(a.difference(b))
        else:
            raise TypeError("a and b should be sets")

    print("Checking if B is a subset of A")
    subset_check(a, b)
    print("A - B")
    dif_in_sets(a, b)
    print("Giving you the cross product of A and B: A x B")
    cross_product(a, b)
    return "Thank you and goodbye"


# # test case 1 Uncomment lines below to test
# x = "a"
# y = {"f", "e", "d", "c", "b", "a"}
#
# print(subset_check(y, x))

# test case 2
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

print(set_functions(y, x))
