#Tuple

'''tup=(1,2,3)
print(tup)

(a,b,c)=tup
print(a)
print(b)
print(c)
print()
for i in tup:
    print(i)'''

'''tup1=(1,2,3)
tup2=(4,5,6,7)
tup3=tup1+tup2
print(tup3)
print(len(tup1))
print(len(tup2))
print(len(tup3))
print(min(tup3))
print(max(tup3))

tup1=(10,20,30,40,50)
print(tup1[1])
print(tup1[-3])
print(tup1[0:3])'''

'''lst=[1,2,3,4]
tup1=tuple(lst)
print(tup1)'''

'''tup=(10,11,8,0,1,15,-1)
lst=[]
for i in range(0,max(tup)):
    lst.append(min(tup))
print(lst)'''

tup1=('-','+','*','$')
tup2=(10,2,1,0,11,-1,8)
loc=0
max=max(tup2)
for i in range(0,len(tup1)):
    if(tup1[i]=='*'):
        lc=i
        loc=lc+1
print(loc)
if(loc==0):
    print("There is no * ")
else:
    p=max
    for i in range(1,max+1):
        for k in range(1,p):
            print(" ",end="")
        for j in range(1,i+1):
              print(tup1[lc],end=" ")
        print()
        p-=1
    
    

