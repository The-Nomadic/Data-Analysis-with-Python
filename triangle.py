n=int(input("Enter the limit-"))


print("Pattern 1")
for i in  range(n):
    for j in range(i+1):
        print("*",end=" ")
    print(" ")


print("Pattern 2")
m=n
for i in range(n):    
    for j in range(m):  
        print("*", end=' ') 
    m=m-1 
    print(" ") 


print("Pattern is")
m=n-1
for i in range(n):
    for j in range(m):
        print(end=" ")
    m=m-1
    for j in range(i+1):
        print("*",end=" ")
    print()


print("patter is")
for i,j in zip(range(0,n), range(n,0,-1)):
    print(i*" ",j*"*")