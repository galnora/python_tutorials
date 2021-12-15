# import random
# from random import randint

# def remainder (a,b):
    
#     if a >= b and (b != 0 or b < 0):
#         return print(a % b)
#     elif b > a and (a != 0 or a < 0):
#         return print(b % a)
#     elif a == 0 or b == 0:
#         return None
# remainder(randint(-1000,1000),randint(-1000,1000))

# def repeat_str(repeat, string):
#     return print(repeat*string)

# repeat_str(3,"str")


# def count_sheeps(sheep):
#     # a = 0
#     # for nn in sheep:
#     #     if nn == 'True':
#     #         a = a +1
#     # return print(a)
#     a=sheep.count('True')
#     return print(a)
    

# array1 = ['True', 'True', 'True', 'False', 'True', 'True', 'True', 'True', 'True', 'False']

# count_sheeps(array1)

# def boolean_to_string(b):
#     b = str(b)
#     return b

# boolean_to_string(True)

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

# if len(a)>len(b):
#     for nn in a:
#         print(nn)
# for m in b:
import string

alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)

my_list = []
for nn in alphabet_list:
    for m in a:
        if nn == m:
            if not m in my_list:
                my_list.append(m)
        else:
            for i in b:
                if nn == i:
                    if not i in my_list:
                        my_list.append(i)
print(my_list)

