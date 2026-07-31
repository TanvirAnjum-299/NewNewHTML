#Define A function to greet the customer
def greet_custumer() -> None:
    print("Welcome to the Lemonade Stand")
    print("Lemonade,made for you")
#Call the function
greet_custumer()
#The Price per cup & the number of cups sold
price_per_cup=float(input("Enter the price of cup:"))
cups_sold=int(input("Enter the number of cups sold:"))
#Define A function that returns to total costs
def calculate_total(price,cups):
    total=price*cups
    return total
#Call the function
total: float = calculate_total(price_per_cup, cups_sold)
print("Total revenue:", total)
#Use a function to round up the total & print it
rounded_total=round(total,2)
print("total:",rounded_total)
#How much money the customer paid
amount_paid=float(input("Enter the amount:"))
#Define A function that makes change due return
def calculate_change(paid,total):
    change=paid-total
    return change
#call calculate_change and store the value when it returns
change_due=calculate_change(amount_paid,rounded_total)
rounded_change=round(change_due,2)
print(rounded_change)