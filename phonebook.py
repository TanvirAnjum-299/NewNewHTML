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
        if j==4:
           temp.append(str(input("Enter Category(Family/Friends/Work/Others):")))
           if temp[j]=='' or temp[j]=='':
              temp[j]=None
        #that means phone_book is a 2-D array and temp is a 1-D array
    print(phone_book)
    return phone_book
def menu():
   print("*******************************************************")
   print("Smartphone Directory")
   print("*******************************************************")
   print("You can perform the following operations in this phonebook")
   print("1.Add a new contact")
   print("2.Remove an existing contact")
   print("3.Delete all contacts")
   print("4.Search for a contact")
   print("5.Display all contacts")
   print("6.Exit Phonebook")
   choice=(int(input("Please enter your choice:")))
   return choice
def add_contact(pb):
   dip=[]
   for i in range(len(pb[0])):
      if i==0:
         dip.append(str(input("Enter Name:")))
      if i==1:
         dip.append(int(input("Enter Number:")))
      if i==2:
         dip.append(str(input("Enter a e-Mail adress")))
      if i==3:
         dip.append(str(input("Enter date of birth (dd/mm/yy):")))
      if i==4:
         dip.append(str(input("Enter Category(Family/Friends/Work/Others):")))
   pb.append(dip)
def remove_existing(pb):
   query=str(input("Please enter the name of the contact you wish to remove"))
   for i in range(len(pb)):
      if query==pb[i][0]:
         temp +=1
         print(pb.pop(i))

