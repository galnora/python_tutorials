#Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent 
#numbers in the array.
#def adjacent_element_product(array):
array=[1,2,6,8,9,6,3,5,7,8,6,15]
a=0
for nn in range(len(array)):
    if (nn+1) < len(array):
        if (array[nn]*array[nn+1])>a:
            a = array[nn]*array[nn+1]
print(a)
print(max(array))









#adjacent_element_product([1,2,6,8,9,6,3,5,7,8,6])
