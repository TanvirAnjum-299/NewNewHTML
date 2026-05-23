file_read=open('codingal.txt','r')
print("File in read mode-")
print(file_read.read())
file_read.close()



file_write=open('codingal.txt','w')
file_write.write("File in writing mode.......")
file_write.write("Hi! I am Penguin & I am 1 year old")
file_write.close()


file_append=open('codingal.txt','a')
print("\n File in append mode.....")
file_append.write("Hi, I am Penguin & I am 1 year old")
file_append.close