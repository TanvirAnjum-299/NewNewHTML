#define a function to calculate cube
def cube(number):
    return number*number*number
#define a function to check divisibility by 3
def by_three(number):
    if number %3==0:
        return cube(number)
    else:
        return "Number is not divisible by 3"
#display_result
print(by_three(9))
print(by_three(4))