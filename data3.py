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
