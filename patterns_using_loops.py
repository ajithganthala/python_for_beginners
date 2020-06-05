'''n=int(input("Enter n"))
for i in range(1,n+1):
      for j in range(1,i+1):
          print("*",end=" ")
      print()'''

'''
n=int(input("Enter n "))
p=n
for i in range(1,n+1):
    for k in range(1,p):
        print(" ",end="")
    for j in range(1,i+1):
          print("*",end=" ")
    print()
    p-=1


n=int(input("Enter n "))
p=n
for i in range(1,n+1):
    for k in range(1,p):
        print(" ",end="")
    for j in range(1,i+1):
          print(j,end=" ")
    print()
    p-=1


n=int(input("Enter n "))
p=n
for i in range(1,n+1):
    for k in range(1,p):
        print(" ",end="")
    for j in range(1,i+1):
          print(i,end=" ")
    print()
    p-=1


n=int(input("Enter n "))
for i in range(1,11,2): #2 is step(increment),default is 1
    print(n,"*",i,"=",n*i)'''


#While loop

'''n=int(input("Enter n"))
i=1
j=1
while(i<=n):
    while(j<=i):
          print("*",end=" ")
          j+=1
    print()
    i+=1
    j=1'''


'''n=int(input("Enter n "))
i=1
p=n
j=1
k=1
while(i<=n):
    while(k<p):
        print(" ",end="")
        k+=1
    while(j<=i):
          print("*",end=" ")
          j+=1
    print()
    i+=1
    j=1
    k=1
    p-=1'''
