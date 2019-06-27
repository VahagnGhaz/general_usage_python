# wrong
def add_num(num, num_list=[]):
    num_list.append(num)
    return num_list


print(add_num(1))  # prints [1]
print(add_num(2))  # prints [1,2]


# correct
def add_num(num, num_list=None):
    if not num_list:
        num_list = []  # not in the same memory as default num_list
    num_list.append(num)
    return num_list


print(add_num(1))  # prints [1]
print(add_num(2))  # prints [2]


# explanation: list (also set, dict) is mutable (means: its state can be changed )
#              default argument is 'evaluated' once, during func call for the first time (but 'set' for every func call)
#              add_num.__defaults__ keeps num_list argument in memory, and if it changes, changes also in __defaults__



