

number1 = int(input("Pick a number: "))
number2 = int(input("Pick another number: "))

def GCF(number1,number2):
    if number1 < number2:
        smaller_number = number1
    else:
        smaller_number = number2

    for i in range(1, smaller_number + 1):
        if (number1 % i == 0) and (number2 % i == 0):
          gcf = i

    return gcf

print("The Greatest common factor of number 1 and 2 is: ", GCF(number1, number2))

