#You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal
# to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.
arr=[1,2,3,4,3,2,1]
# list=[]
# for nn in range(len(arr)):
#     a= sum(arr[0:nn])
#     b= 0
#     for m in range(len(arr)):
#         if m>nn:
#             b += arr[m]
#     if a == b:
#         list.append(nn)
# if len(list)>0:
#     print(list[0])
# else:
#     print("-1")

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1


