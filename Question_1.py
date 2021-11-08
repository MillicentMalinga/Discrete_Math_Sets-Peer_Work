#initialize list and set
my_list = ['Alex', 'Bob', 'Sam', 'Brian', 'Brian', 'Sam', 'Sam']
my_set =set(my_list)

#function to test
'''If statement checks whether list elements constitutes set. Outputs True when the given list elements constitues the set,
and false when they do not. When True no other statement displayed. When false, False is displayed plus the true set'''
def check(lst):
    if lst in my_set:
        return True
    else:
        return False
print(False,", the set should be:",my_set)
