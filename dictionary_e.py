#Write a Python script to concatenate following dictionaries to create a new one.
# Manan Pathak(20CS060)
#https://github.com/Manan060/CE259_PIP.git
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
dict4 = {}
for d in (dict1, dict2, dict3): dict4.update(d)
print(dict4)

