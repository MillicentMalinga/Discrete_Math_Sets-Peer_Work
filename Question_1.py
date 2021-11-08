my_list = ['Alex', 'Bob', 'Sam', 'Brian', 'Brian', 'Sam', 'Sam']
my_set =set(my_list)

def check(lst):
    if lst in my_set:
        return True
    else:
        return False
print(False,", the set should be:",my_set)
