    #they are pretty like lists but they are immutable, meaning that you can't change them after they are created
    
my_list = [1,2,3]

my_tuple = (1,2,3)

other_tuple = 1,2

my_list[1] = 4

print(my_list)

try:
    my_tuple[1] = 4
except TypeError as e:
    print('You can´t change a tuple after it is created', e)
    
def sum_and_product(x,y):
    return (x+y),(x*y)
sp = sum_and_product(2,3)
print(sp)
    
s,p = sum_and_product(5,10)
print(s,p)

x,y = 1,2
print(x,y)
x,y = y,x
print(x,y)