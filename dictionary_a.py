#Write a Python script to check whether a given key already exists in a dictionary.
# Manan Pathak(20CS060)
#https://github.com/Manan060/CE259_PIP.git
dict = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
def key_inDict(x):   #function to check if key is present in dictionary or not
  if x in dict:
      print('Key is Present')
  else:
      print('Key is not Present')
key_inDict(4)
key_inDict(7)
print('-20CS060')