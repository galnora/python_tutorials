#Write a function that accepts an array of 10 integers (between 0 and 9), 
#that returns a string of those numbers in the form of a phone number.
number = [1,2,3,4,5,6,7,8,9,0]
# string=""
# for nn in range(len(number)):
#     if nn == 0:
#         string += "("
#     string += str(number[nn])
#     if nn == 2:
#         string += ") "
#     if nn == 5:
#         string += "-"
# print(string)
print("({}{}{}) {}{}{}-{}{}{}{}".format(*number))