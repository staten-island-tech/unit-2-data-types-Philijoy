#booleans
x = False

def check(x):
    if (x== True):
        print("is logged in")
    else:
        print("please log in")
check(x)

def add(x,y):
    print(x + y)
add(45,35)

#booleans and control
day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")


#Strings "a,b,c"
def message(name):
    print(name)
message("meow")
x = "1"
int(x)

#strings and data is different
add("35","45")

#strings
x= "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)

temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')