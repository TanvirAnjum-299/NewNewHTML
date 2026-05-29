with open('codingal.txt','w')as file:
    file.write("Hi! I am Jarif, I am 12 year old")
file.close()


with open('codingal.txt','r')as file:
    data=file.readlines()
    print("The words in this file are...")

    for line in data:
        word=line.split()
        print(word)