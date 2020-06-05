#repeated elements in a list
'''
a=[1,2,3,4,5]
b=[3,4,5,6,7,8]
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if(a[i]==b[j]):
            print("The repeated elements are ",a[i],end=" ")
            print()
'''
p=0
a=[]
b=[]
n=int(input("Enter number of elements in a: "))
for i in range(0,n):
      a.append(input("\nEnter elements of a "))
m=int(input("Enter number of elements in b: "))
for i in range(0,m):
      b.append(input("\nEnter elements of b "))
print(a)
print(b)
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if(a[i]==b[j]):
            print("The repeated elements are ",a[i],end=" ")
            print()
            p+=1
if(p==0):
    print("There are no repeated elements")

