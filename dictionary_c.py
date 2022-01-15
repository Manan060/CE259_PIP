#Write a Python program to sum all the items in a dictionary
# Manan Pathak(20CS060)
#https://github.com/Manan060/CE259_PIP.git
def dictSum(dict):
     sum=0
     for i in dict.values():
         sum= sum + i
     return sum
dict = {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}
print('Sum of all values : ',dictSum(dict))