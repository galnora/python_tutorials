primes=[]
for nn in range(10000):
    list=[]
    for m in range(nn+1):
        if m>0 and nn%m == 0:
            list.append(m)
    if len(list)==2:
        primes.append(nn)
#print(primes)
import random
from random import randint
a = randint(70,1000)
print(a)
b = (round(a/6 -48))
new_list=[]
for i in range(len(primes)-1):
    result= all(elem in new_list for elem in primes)
    while result is False:
        if primes[i]-b < primes[i+1]-b:
            b=(primes[i])
            new_list=[b,b+4,b+6,b+10,b+12,b+16]
            print(new_list)
        result= all(elem in primes for elem in new_list)
        print(result)

            
list1=[1,2,3,4,5,6]
list2=[1,2,3,4,5,6,7,8,9,10]

result=all(elem in list2 for elem in list1)
print(result)

