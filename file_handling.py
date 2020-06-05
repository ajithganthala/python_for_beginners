'''file=open("ex.txt","r") # r=read w=write a=append r+ =read and write
#print(file.read())
#print(file.readline())
#print(file.readlines())

file=open("ex.txt","w")
file.write("This is the new text")
file.close()
file=open("ex.txt","r")
print(file.read())

file=open("ex.txt","a")
file.write("This is the another text")
file.close()
file=open("ex.txt","r")
print(file.read())'''


file=open("ex.txt","r")
e=file.read()
file=open("ex1.txt","w")
file.write(e)
file.close()
file=open("ex1.txt","r")
print(file.read())
