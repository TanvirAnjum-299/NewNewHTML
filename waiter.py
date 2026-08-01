bill_amount=float(input("Enter bill amount:"))
tip_perc=int(input("Enter the tip percentage:"))
def total_calc(bill_amount,tip_perc):
    total=bill_amount+((tip_perc/100)*bill_amount)
    total=round(total,2)
    print(f"Please pay ${total}")
total_calc(bill_amount,tip_perc)