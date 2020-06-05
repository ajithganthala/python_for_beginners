d={"p1":1000,"p2":1200,"p3":1700,"p4":1400,"p5":2450,"p6":2100}
for i in d:
    print(i)
print()
for i in d.values():
    print(i)
print()
for i in d:
    print(d[i])
print()
d["p1"]=1234
for i in d:
    print(i)
print()
for i in d.values():
    print(i)
print()
for i,j in d.items():
    print(i,j)
print()
print(len(d))
if "p1" in d:
    print("Name is in dictionary")
else:
    print("Name is not in the dictionary")

'''
d["Institute"]="Aditi" #to add
for i,j in d.items():
    print(i,j)
print()
d.pop("p6")             #it will remove 
for i,j in d.items():
    print(i,j)
print()
d.popitem()             #it will remove 
for i,j in d.items():
    print(i,j)
print()''''


    

