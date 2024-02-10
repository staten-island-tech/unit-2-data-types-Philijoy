def all_factors(x): 
    print("The factors are: ")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

number = 125
all_factors(number)