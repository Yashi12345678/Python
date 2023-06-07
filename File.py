 filename=input("enter the name of the file with the correct path")

t=input("enter the existing string")

with open(filename,"r") as f:

filedata=f.read()

word_count=filedata.count(t)

print("the word occurs ",word_count,"times")

filedata=filedata.replace(t,"")

with open("c:/pythonprgs/test.txt","w") as f:

f.write(filedata)
