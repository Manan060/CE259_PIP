#Write a Python program to convert a tuple to a string
# Manan Pathak(20CS060)
#https://github.com/Manan060/CE259_PIP.git
def tupleToStr(tup):
    str = ''.join(tup)
    return str
 
 

tuple1 = ('c', 'h', 'a', 'r', 'u','s','a','t')
str = tupleToStr(tuple1)
print(str)