def calculate_gcf(x,y):
    while y!=0:
         z=y
         y=int(x)%int(x)
         x=z
         return z

num1 = int(input("give a number: "))
num2 = int(input("give another number: "))
gcf = calculate_gcf (1, 2)
print("The greatest common factor of number 1 and 2 is: ")
