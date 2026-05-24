file=open("Codingal.txt","r")
counter=0
Content=file.read()
CoList=Content.split("\n")
print(CoList)
for i in CoList:
    if i:
        counter=counter+1
print("This is the number of lines in the file")
print(counter)