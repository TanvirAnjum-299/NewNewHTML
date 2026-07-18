print("===ATM Cash Dispenser===\n")
total_100=total_50=total_20=total_10=total_5=total_1=0
customers_served=0
total_dispensed=0
serving=True
while serving:
    name=input("Enter customer name:")
    amount=int(input(f"Hello{name}!Enter withdrawal amount:"))
    if amount<=0:
        print("Invalid amount.Please enter a positive number.\n")
        continue
    print(f"\nDispensing{amount}units for{name}:")
    remaining=amount
    idx=1
    

