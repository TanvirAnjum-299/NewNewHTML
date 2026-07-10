medicalcause=input("Did you have a medical cause?(Y/N):").strip().upper()

if medicalcause=='Y':
    print("You are allowed to give the exam")
else:


    attendance=int(input("Enter the attendance of the student:"))
    
if attendance>=75:  #Condition 2
    
    print("Allowed to give the exam")
else:
    print("Not allowed to give the exam")