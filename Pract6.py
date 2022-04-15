'''
    20CS060
    Manan Pathak
'''
t = int(input())
l = {}
for i in range(t):
    n = input()
    if n in l:
        l[n]+=1
    else:
        l[n] = 1
print(len(l))
for i in l:
    print(l[i], end=" ")