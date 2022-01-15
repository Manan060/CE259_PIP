#Write a Python script to merge two Python dictionaries.
# Manan Pathak(20CS060)
#https://github.com/Manan060/CE259_PIP.git
dict1={'a':2,'b':4}
dict2={'p':6,'q':8}
dict=dict1.copy()
dict.update(dict2)
print(dict)