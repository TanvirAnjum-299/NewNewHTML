import sys
def initial_phonebook():
    rows,columns=int(input("Please Enter the initial Number of contacts")),5
    phone_book=[]
    print(phone_book)
    for i in range(rows):
        print("\n Enter contact %d details in the following order(Only):"%(i+1))
        print("NOTE: * indicates mandatory fields") 
    print("....................................................................")
    temp=[]
    for j in range(columns):
        if j==0:
            temp.append(str(input("Enter Name*:")))
            if temp[j]=='' or temp[j]=='':
                sys.exit("Name is a mandatory.Process exiting due to blank field...")
        if j==1:
         temp.append(int(input("Enter Name*:")))
        if j==2:
            temp.append(str(input("Enter e-mail adress:")))
            if temp[j]=='' or temp[j]=='':
                temp[j]=None
        if j==3:
          temp.append(str(input("Enter date of Birth(dd/mm/yy):")))
          if temp[j]=='' or temp[j]=='':
             temp[j]=None
