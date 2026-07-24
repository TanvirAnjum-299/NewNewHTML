print("Half Pyramid Pattern of stars(*):")
rows=int(input("enter the number of rows:"))
for i in range(rows):#rows=5, i=0, 1, 2, 3, 4
    for j in range(i+1):
        print("*",end="")
    print()