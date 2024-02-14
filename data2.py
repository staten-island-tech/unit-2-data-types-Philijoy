# Challenge develop a function that accepts a the user input and will tell you how many words are in that string.
x = input("input a sentence") 
y= x.split()

words = len((x.split)())
print("number of words: ", words)


# tip calculator 
bill = float(input("Enter your bill:"))
tip = int(input("Enter your tip:"))

print("bill = ", bill)
print("tip = ", tip)
print("total = ", bill + tip)


#challenge: create a function that determines if a number is odd or even
x = input("give number") 
if (int (x)%2) == 0:
    print("even")
else:
    print("odd")
#odd and even
print(4350%2)


# challenge:Create a function to accept a "bill" value and offer a tip of 0%, 15%, 20% or 25% depending if the service was "bad, okay, good , or great ". 
service = x
if service == 0:
    print("This service is bad")
elif service == (15):
    print("The service is okay")
elif service == (20):
    print("The service is good")
else: (25)
print("The service is great")


#Challenge: Create a function that accepts an input and determines all factors of the number
<<<<<<< HEAD
def all_factors(x):
    print("factors of x " "are:")
    for i in range(1, x+1):
        if x % i == 0:
          print(i)

number = 25

all_factors (number)

#Challenge: Create a function that accepts 2 arguments. Find the greatest common factor between those numbers.
number1 = int(input("give a number: "))
number2 = int(input("give another number: "))
gcf = calculate_gcf (number1, number2)
print("The greatest common factor ")
=======
def all_factors(x): 
    print("The factors are: ")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

number = 125
all_factors(number)


#Challenge: Create a function that accepts 2 arguments. Find the greatest common factor between those numbers.
factor = int(input ("Give number "))
factor1 = int(input ("Give number "))

def greatest_factor(x): 
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
values = greatest_factor(factor)
print('Factoring next #')
values1 = greatest_factor(factor1)
Gcf = [values, values1] 
print(Gcf)
>>>>>>> 1078eeefb3621422d2b60d0bdc9b47fdb644f3fe

factors = []
factors.append
print(factors[-1])
