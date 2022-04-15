'''
    20CS060
    Manan pathak
'''
n=int(input())
for i in range(n):
    m=input()
    n=len(m)
    m1=m[:n//2]
    if(n%2==0):
        m2=m[n//2:]
    else:
        m2=m[n//2+1:]
    if(sorted(m1)==sorted(m2)):
        print("YES")
    else:
        print("NO")