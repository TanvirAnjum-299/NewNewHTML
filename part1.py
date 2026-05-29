with open('codingal.txt','w')as file:
    file.write("Hi! I am Jarif, I am 12 year old.")
file.close()


with open('codingal.txt','r')as file:
    data=file.readlines()
    print("The words in this file are...")

    for line in data:
        word=line.split()
        print(word)
file_append=open('codingal.txt','a')
print("\n File in append mode.....")
file_append.write("Hi, I am Penguin & I am 1 year old")
file_append.close