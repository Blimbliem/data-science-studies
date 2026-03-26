# its problabily the most used data structure in python, the lists.

# we can resume saying that lists are a sorted collection of items.

interger_list = [1,2,3,4]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [interger_list, heterogeneous_list, []]
list_length = len(interger_list)
list_sum = sum(interger_list)

x = [0,1,2,3,4,5,6,7,8,9]
zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]
x[0] = -1 

first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]

every_third = x[::3]
five_to_three = x[5:2:-1]

#python have an operator to check if an item is in a list, the 'in' operator
# we should use this operator when the time of execution dont matter or when we are working with small lists, because the 'in' operator has a time complexity of O(n)
1 in [1,2,3]
0 in [1,2,3]

# to modificate lists we can use the 'extends'
x = [1,2,3]
x.extend([4,5,6])

#if you don´t want modify 'x', you can concatenate lists using the '+' operator, but this will create a new list and will have a time complexity of O(n)
y = x + [7,8,9]

# or we can use the 'append' operator, to increase the list one by one

x.append(0)
y = x[-1]
z = len(x)

# we can unpack the list when the value inside it is known

x,y = [1,2]

# we can use the underline to ignore values

_,y = [1,2]# y == 2
