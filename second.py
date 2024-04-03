

def function(number):
    if number%2==0:
        return "the number is even!"
    elif number%2==0 and number%4!=0:
        return "the number can be divided by 4"
    elif number%2!=0:
        return "the number is odd"
    
    
def checking_function(number, number2):
    if number%number2==0:
        return "the first number can be divided by second number"
    else:
        return "the first number cannot be divided by second number"
    

    
while True:
    number=int(input("insert the first number: "))
    number2= int(input("insert the second number:"))
    print(function(number),checking_function(number, number2))
    break
    

    


print(function(number))
